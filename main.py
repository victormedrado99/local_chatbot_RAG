import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import threading
import queue
import os
import sys

# Desabilitar telemetria do ChromaDB
os.environ['ANONYMIZED_TELEMETRY'] = 'False'
os.environ['CHROMA_TELEMETRY'] = 'False'

# Patch para evitar erros de módulos faltando no executável
try:
    import chromadb.telemetry.product.posthog
except (ImportError, ModuleNotFoundError):
    # Criar módulo dummy se não existir
    import types
    import chromadb
    if not hasattr(chromadb, 'telemetry'):
        chromadb.telemetry = types.ModuleType('telemetry')
    if not hasattr(chromadb.telemetry, 'product'):
        chromadb.telemetry.product = types.ModuleType('product')
    if not hasattr(chromadb.telemetry.product, 'posthog'):
        chromadb.telemetry.product.posthog = types.ModuleType('posthog')
    sys.modules['chromadb.telemetry'] = chromadb.telemetry
    sys.modules['chromadb.telemetry.product'] = chromadb.telemetry.product
    sys.modules['chromadb.telemetry.product.posthog'] = chromadb.telemetry.product.posthog

# Patch para chromadb.api.rust
try:
    import chromadb.api.rust
except (ImportError, ModuleNotFoundError):
    import types
    import chromadb
    if not hasattr(chromadb, 'api'):
        chromadb.api = types.ModuleType('api')
    if not hasattr(chromadb.api, 'rust'):
        # Criar módulo rust dummy
        chromadb.api.rust = types.ModuleType('rust')
    sys.modules['chromadb.api'] = chromadb.api
    sys.modules['chromadb.api.rust'] = chromadb.api.rust

from langchain_community.llms import Ollama
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Importar cross-encoder para re-ranking
try:
    from sentence_transformers import CrossEncoder
    RERANK_SUPPORT = True
except ImportError:
    RERANK_SUPPORT = False
    print("Aviso: sentence-transformers não instalado. Re-ranking desabilitado.")

# Tentar importar loader para DOCX (opcional)
try:
    from langchain_community.document_loaders import Docx2txtLoader
    DOCX_SUPPORT = True
except ImportError:
    DOCX_SUPPORT = False

# Small lightweight Document-like class for text files (avoids importing langchain schema at runtime)
class LocalDocument:
    def __init__(self, page_content: str, metadata: dict | None = None):
        self.page_content = page_content
        self.metadata = metadata or {}

DB_PATH = './meu_armazem_chroma'
EMBED_MODEL = 'nomic-embed-text'
LLM_MODEL = 'deepseek-r1:8b'

class ChatbotRAGGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Chatbot RAG')
        self.root.geometry('1000x700')
        self.root.configure(bg='#2b2b2b')
        
        self.output_queue = queue.Queue()
        self.processing = False
        
        # Controle de remoção de documentos
        self.awaiting_removal_input = False
        self.pending_removal_list = None
        
        # Inicializar componentes LangChain uma única vez
        self.llm = None
        self.embeddings = None
        self.db = None
        self.rag_chain = None
        self.reranker = None  # Cross-encoder para re-ranking
        
        self.setup_style()
        self.create_widgets()
        self.check_queue()
        
        # Iniciar a inicialização pesada em uma thread DEPOIS de criar widgets
        self.output_queue.put(('__BOT__', 'Inicializando modelos... Isso pode levar um momento.\n'))
        threading.Thread(target=self.initialize_components, daemon=True).start()
        
    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Dark.TFrame', background='#2b2b2b')
        style.configure('Dark.TLabel', background='#2b2b2b', foreground='white')
        style.configure('Dark.TButton', background='#404040', foreground='white')
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style='Dark.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        title = ttk.Label(main_frame, text='Chatbot RAG', style='Dark.TLabel')
        title.pack(pady=(0, 10))
        
        btn_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(btn_frame, text='Adicionar Documento', command=self.add_pdf).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Listar Arquivos', command=self.list_files).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Remover Documento', command=self.remove_document).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Ajuda', command=self.show_help).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Limpar', command=self.clear_terminal).pack(side=tk.RIGHT)
        
        term_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        term_frame.pack(fill=tk.BOTH, expand=True)
        
        # Terminal com input integrado
        self.terminal_output = scrolledtext.ScrolledText(
            term_frame, 
            height=20, 
            bg='#1e1e1e', 
            fg='#00ff00',  # Verde padrão para bot
            font=('Courier New', 10),  # Courier New funciona melhor com cores
            wrap=tk.WORD,
            insertbackground='#00ff00',  # Cursor verde
            state='normal'  # Sempre normal para permitir edição
        )
        self.terminal_output.pack(fill=tk.BOTH, expand=True)
        
        # Configurar tags de cores com MAIOR PRIORIDADE
        self.terminal_output.tag_configure('bot_color', foreground='#00ff00')  # Verde
        self.terminal_output.tag_configure('user_color', foreground='#00bfff')  # Azul
        self.terminal_output.tag_configure('source_color', foreground='#ffa500')  # Laranja
        self.terminal_output.tag_configure('prompt_color', foreground='#ffffff')  # Branco
        
        # REMOVER tag_raise - não é necessário e pode causar problemas
        
        # Bind de teclas para o terminal
        self.terminal_output.bind('<Return>', self.handle_input)
        self.terminal_output.bind('<KeyPress>', self.on_key_press)
        
        # Variável para rastrear a linha de input
        self.input_start = '1.0'
        
        # Mensagens de boas-vindas usando a fila (garantindo que as tags existem)
        self.output_queue.put(('__BOT__', 'Bem-vindo ao Chatbot RAG!\n'))
        self.output_queue.put(('__BOT__', 'Digite sua pergunta e pressione Enter.\n\n'))
        self.output_queue.put('__SHOW_PROMPT__')
        
    def write_to_terminal(self, text, bot=True, color_tag=None):
        """Escreve no terminal com cor apropriada"""
        # Pegar posição ANTES de inserir (importante!)
        start_idx = self.terminal_output.index("end-1c")
        
        # Inserir o texto
        self.terminal_output.insert(tk.END, text)
        
        # Pegar posição DEPOIS de inserir
        end_idx = self.terminal_output.index("end-1c")
        
        # Aplicar tag de cor (se especificada)
        if color_tag:
            self.terminal_output.tag_add(color_tag, start_idx, end_idx)
        
        # Auto-scroll para o fim
        self.terminal_output.see(tk.END)
        
    def show_prompt(self):
        """Mostra o prompt de comando"""
        if not self.processing:
            # Inserir quebra de linha primeiro
            self.terminal_output.insert(tk.END, '\n')
            
            # Inserir prompt ">" e aplicar cor APENAS ao prompt
            prompt_start = self.terminal_output.index(tk.END + '-1c')
            self.terminal_output.insert(tk.END, '> ')
            prompt_end = self.terminal_output.index(tk.END + '-1c')
            self.terminal_output.tag_add('prompt_color', prompt_start, prompt_end)
            
            self.terminal_output.see(tk.END)
            self.input_start = self.terminal_output.index(tk.END + '-1c')
    
    def on_key_press(self, event):
        """Impede edição do texto anterior ao prompt"""
        if self.processing:
            return 'break'
        
        # Permitir apenas editar após o prompt
        current_pos = self.terminal_output.index(tk.INSERT)
        if self.terminal_output.compare(current_pos, '<', self.input_start):
            self.terminal_output.mark_set(tk.INSERT, tk.END)
            return 'break'
    
    def handle_input(self, event):
        """Processa o input quando Enter é pressionado"""
        if self.processing:
            return 'break'
        
        # Pegar o texto digitado após o prompt
        user_input = self.terminal_output.get(self.input_start, tk.END).strip()
        
        if user_input:
            # Exibir a mensagem do usuário em azul
            self.terminal_output.insert(tk.END, '\n')
            self.output_queue.put(('__USER__', f'👤 Você: {user_input}\n\n'))
            
            # Verificar se estamos aguardando input para remoção
            if self.awaiting_removal_input:
                self.processing = True
                threading.Thread(target=self._process_removal_selection, args=(user_input,), daemon=True).start()
            else:
                # Processo normal de chat
                self.processing = True
                threading.Thread(target=self._chat_worker, args=(user_input,), daemon=True).start()
        else:
            # self.terminal_output.insert(tk.END, '\n') # Evita linha extra
            self.show_prompt()
        
        return 'break'  # Impede a quebra de linha padrão
        
    def clear_terminal(self):
        self.terminal_output.delete(1.0, tk.END)
        self.write_to_terminal('Terminal limpo!\n\n', color_tag='bot_color')
        self.processing = False
        self.show_prompt()
        
    def add_pdf(self):
        # Aceitar múltiplos formatos
        filetypes = [
            ('Todos Documentos', ('*.pdf', '*.txt', '*.md', '*.docx')),
            ('PDF', '*.pdf'),
            ('Texto', '*.txt'),
            ('Markdown', '*.md')
        ]
        if DOCX_SUPPORT:
            filetypes.append(('Word', '*.docx'))
            
        file_path = filedialog.askopenfilename(title='Selecione documento', filetypes=filetypes)
        if file_path:
            self.write_to_terminal(f'\nAdicionando {file_path}...\n', color_tag='bot_color')
            threading.Thread(target=self._add_pdf_worker, args=(file_path,), daemon=True).start()
            
    def _add_pdf_worker(self, file_path):
        try:
            # Garantir inicialização do DB se ainda não estiver pronta
            if self.db is None:
                try:
                    self.output_queue.put(('__BOT__', '⏳ Inicializando banco de dados...\n'))
                    self.embeddings = OllamaEmbeddings(model=EMBED_MODEL)
                    self.db = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings)
                    # Rebuild rag chain with new db
                    if self.llm is None:
                        self.llm = Ollama(model=LLM_MODEL)
                    self._build_rag_chain()
                except Exception as e:
                    self.output_queue.put(('__BOT__', f'❌ Erro ao inicializar DB: {str(e)}\n'))
                    return

            ext = os.path.splitext(file_path)[1].lower()
            
            # Carregar documento baseado na extensão
            self.output_queue.put(('__BOT__', f'📄 Carregando arquivo {ext}...\n'))
            
            if ext == '.pdf':
                loader = PyMuPDFLoader(file_path)
                docs = loader.load()
            elif ext == '.txt':
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                docs = [LocalDocument(page_content=text, metadata={'source': file_path})]
            elif ext == '.md':
                try:
                    loader = UnstructuredMarkdownLoader(file_path)
                    docs = loader.load()
                except Exception:
                    # Fallback para leitura simples
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        text = f.read()
                    docs = [LocalDocument(page_content=text, metadata={'source': file_path})]
            elif ext == '.docx' and DOCX_SUPPORT:
                loader = Docx2txtLoader(file_path)
                docs = loader.load()
            else:
                supported = 'PDF, TXT, MD' + (', DOCX' if DOCX_SUPPORT else '')
                self.output_queue.put(('__BOT__', f'❌ Formato não suportado. Use: {supported}\n'))
                return

            # Dividir em chunks com feedback
            self.output_queue.put(('__BOT__', f'✂️  Dividindo em chunks...\n'))
            # Chunks menores = busca mais precisa e re-ranking mais eficaz
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=600,        # Reduzido de 1000 para 600
                chunk_overlap=100,     # Reduzido de 150 para 100
                separators=["\n\n", "\n", ". ", " ", ""]
            )
            chunks = splitter.split_documents(docs)
            
            total_chunks = len(chunks)
            self.output_queue.put(('__BOT__', f'📊 Total de chunks: {total_chunks}\n'))
            
            # Adicionar chunks com feedback de progresso
            self.output_queue.put(('__BOT__', f'🔄 Gerando embeddings e adicionando ao banco...\n'))
            
            # Para arquivos grandes, adicionar em lotes para dar feedback
            batch_size = 50
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i+batch_size]
                self.db.add_documents(batch)
                progress = min(i + batch_size, total_chunks)
                self.output_queue.put(('__BOT__', f'   Processado: {progress}/{total_chunks} chunks\n'))
            
            self.output_queue.put(('__BOT__', '✅ Arquivo adicionado com sucesso!\n'))
        except Exception as e:
            self.output_queue.put(('__BOT__', f'❌ Erro: {str(e)}\n\n'))
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
            
    def show_help(self):
        self.write_to_terminal('\n=== AJUDA ===\n', color_tag='bot_color')
        self.write_to_terminal('1. "Adicionar Documento" - Carregar PDF, TXT, MD ou DOCX\n', color_tag='bot_color')
        self.write_to_terminal('2. "Listar Arquivos" - Ver documentos no banco\n', color_tag='bot_color')
        self.write_to_terminal('3. "Remover Documento" - Remover arquivo específico\n', color_tag='bot_color')
        self.write_to_terminal('4. Digite sua pergunta após o prompt >\n', color_tag='bot_color')
        self.write_to_terminal('5. Pressione Enter para enviar\n\n', color_tag='bot_color')
        self.write_to_terminal('Formatos suportados: PDF, TXT, Markdown', color_tag='bot_color')
        if DOCX_SUPPORT:
            self.write_to_terminal(', DOCX\n\n', color_tag='bot_color')
        else:
            self.write_to_terminal('\n\n', color_tag='bot_color')
        self.show_prompt()
    
    def list_files(self):
        self.write_to_terminal('\nListando arquivos no armazem...\n', color_tag='bot_color')
        threading.Thread(target=self._list_files_worker, daemon=True).start()
    
    def remove_document(self):
        """Inicia o processo de remoção de documento"""
        self.write_to_terminal('\n🗑️  Preparando lista de documentos para remoção...\n', color_tag='bot_color')
        threading.Thread(target=self._remove_document_worker, daemon=True).start()
    
    def _remove_document_worker(self):
        """Worker para remover documento do banco vetorial"""
        try:
            import os
            if not os.path.exists(DB_PATH):
                self.output_queue.put(('__BOT__', '❌ Armazém ainda não foi criado. Nada para remover.\n\n'))
                return
            
            # Obter lista de documentos únicos
            all_docs = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings).get()
            
            if not all_docs or not all_docs.get('metadatas'):
                self.output_queue.put(('__BOT__', '❌ Armazém está vazio. Nada para remover.\n\n'))
                return
            
            sources = sorted(set(meta['source'] for meta in all_docs['metadatas'] if 'source' in meta))
            
            if not sources:
                self.output_queue.put(('__BOT__', '❌ Nenhum arquivo encontrado.\n\n'))
                return
            
            # Mostrar lista de arquivos
            self.output_queue.put(('__BOT__', '\n=== Documentos Disponíveis ===\n'))
            for idx, source in enumerate(sources, 1):
                self.output_queue.put(('__BOT__', f'{idx}. {source}\n'))
            self.output_queue.put(('__BOT__', '\n📝 Digite o número do documento para remover (ou "cancelar"):\n'))
            
            # Armazenar lista temporária para seleção
            self.pending_removal_list = sources
            self.awaiting_removal_input = True
            
        except Exception as e:
            self.output_queue.put(('__BOT__', f'❌ Erro ao listar documentos: {str(e)}\n\n'))
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
    
    def _process_removal_selection(self, selection):
        """Processa a seleção do usuário para remoção"""
        try:
            if selection.lower() == 'cancelar':
                self.output_queue.put(('__BOT__', '❌ Remoção cancelada.\n'))
                return
            
            # Tentar converter para número
            idx = int(selection) - 1
            
            if 0 <= idx < len(self.pending_removal_list):
                source_to_remove = self.pending_removal_list[idx]
                self.output_queue.put(('__BOT__', f'\n🗑️  Removendo: {source_to_remove}...\n'))
                
                # Obter IDs de todos os chunks deste documento
                db = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings)
                all_data = db.get()
                
                # Filtrar IDs que correspondem ao source
                ids_to_delete = [
                    all_data['ids'][i] 
                    for i, meta in enumerate(all_data['metadatas']) 
                    if meta.get('source') == source_to_remove
                ]
                
                if ids_to_delete:
                    db.delete(ids=ids_to_delete)
                    self.output_queue.put(('__BOT__', f'✅ Removido {len(ids_to_delete)} chunks do documento.\n'))
                    self.output_queue.put(('__BOT__', f'✅ Documento "{source_to_remove}" removido com sucesso!\n'))
                else:
                    self.output_queue.put(('__BOT__', '❌ Nenhum chunk encontrado para este documento.\n'))
            else:
                self.output_queue.put(('__BOT__', '❌ Número inválido. Operação cancelada.\n'))
                
        except ValueError:
            self.output_queue.put(('__BOT__', '❌ Entrada inválida. Digite um número ou "cancelar".\n'))
        except Exception as e:
            self.output_queue.put(('__BOT__', f'❌ Erro ao remover: {str(e)}\n'))
        finally:
            self.awaiting_removal_input = False
            self.pending_removal_list = None
            self.output_queue.put('__SHOW_PROMPT__')
    
    def _list_files_worker(self):
        try:
            import os
            if not os.path.exists(DB_PATH):
                self.output_queue.put(('__BOT__', 'Armazem ainda nao foi criado. Adicione um PDF primeiro.\n\n'))
                return
            
            # Re-inicializa o Chroma para garantir que ele leia os dados mais recentes do disco
            all_docs = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings).get()
            
            if not all_docs or not all_docs.get('metadatas'):
                self.output_queue.put(('__BOT__', 'Armazem esta vazio.\n\n'))
                return
            
            sources = set(meta['source'] for meta in all_docs['metadatas'] if 'source' in meta)
            
            if not sources:
                self.output_queue.put(('__BOT__', 'Nenhum arquivo encontrado.\n\n'))
                return
            
            self.output_queue.put(('__BOT__', '\n=== Arquivos no armazem ===\n'))
            for idx, source in enumerate(sorted(sources), 1):
                self.output_queue.put(('__BOT__', f'{idx}. {source}\n'))
            self.output_queue.put(('__BOT__', '\n'))
        except Exception as e:
            import traceback
            error_msg = f'Erro ao listar arquivos: {str(e)}\n'
            self.output_queue.put(('__BOT__', error_msg + '\n'))
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
            
    def _build_rag_chain(self):
        """Cria ou recria a cadeia RAG com o retriever atualizado."""
        retriever = self.db.as_retriever(search_kwargs={'k': 4})
        
        template = 'Responda baseado no contexto:\n\nContexto: {context}\n\nPergunta: {question}\n\nResposta:'
        prompt = ChatPromptTemplate.from_template(template)

        def format_docs(docs):
            return '\n\n'.join(doc.page_content for doc in docs)

        self.rag_chain = ({'context': retriever | format_docs, 'question': RunnablePassthrough()} | prompt | self.llm | StrOutputParser())

    def initialize_components(self):
        """Inicializa os componentes pesados da LangChain."""
        try:
            self.embeddings = OllamaEmbeddings(model=EMBED_MODEL)
            self.db = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings)
            self.llm = Ollama(model=LLM_MODEL)
            
            # Inicializar cross-encoder para re-ranking (se disponível)
            if RERANK_SUPPORT:
                self.output_queue.put(('__BOT__', '📊 Carregando modelo de re-ranking...\n'))
                self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
                self.output_queue.put(('__BOT__', '✅ Re-ranking habilitado!\n'))
            else:
                self.output_queue.put(('__BOT__', '⚠️  Re-ranking desabilitado (instale sentence-transformers)\n'))
            
            self._build_rag_chain()
            self.output_queue.put(('__BOT__', '✅ Modelos prontos para uso!\n'))
        except Exception as e:
            self.output_queue.put(('__BOT__', f'❌ Erro na inicialização: {e}\n'))
            self.output_queue.put(('__BOT__', 'Verifique se o Ollama está rodando com os modelos necessários.\n'))
        finally:
            self.output_queue.put('__SHOW_PROMPT__')

    def _chat_worker(self, query):
        try:
            if not self.rag_chain:
                self.output_queue.put(('__BOT__', '\nModelos ainda não foram inicializados. Aguarde...\n\n'))
                return

            # Mensagem simples de processamento
            self.output_queue.put(('__BOT__', '...\n'))
            
            # Buscar mais documentos inicialmente para ter opções para re-ranking
            initial_k = 10 if self.reranker else 4
            retriever = self.db.as_retriever(search_kwargs={'k': initial_k})
            
            # Recuperar documentos relevantes
            relevant_docs = retriever.invoke(query)
            
            # RE-RANKING: Reordenar documentos usando cross-encoder
            if self.reranker and len(relevant_docs) > 0:
                # Criar pares (query, documento) para scoring
                pairs = [[query, doc.page_content] for doc in relevant_docs]
                
                # Obter scores do cross-encoder
                scores = self.reranker.predict(pairs)
                
                # Ordenar documentos por score (maior = mais relevante)
                doc_score_pairs = list(zip(relevant_docs, scores))
                doc_score_pairs.sort(key=lambda x: x[1], reverse=True)
                
                # Pegar apenas os top 4 após re-ranking
                relevant_docs = [doc for doc, score in doc_score_pairs[:4]]
                
                # Debug: imprimir scores para verificar relevância
                # for idx, (doc, score) in enumerate(doc_score_pairs[:4], 1):
                #     print(f"Doc {idx} - Score: {score:.4f}")
            
            # Construir contexto
            context = '\n\n'.join(doc.page_content for doc in relevant_docs)
            
            # Prompt melhorado para respostas mais precisas
            template = """Responda a pergunta baseando-se APENAS nas informações do contexto fornecido.
Se o contexto não contiver informações suficientes para responder, diga que não há informações suficientes.
Seja direto e preciso na resposta.

Contexto:
{context}

Pergunta: {question}

Resposta:"""
            prompt = ChatPromptTemplate.from_template(template)
            
            chain = prompt | self.llm | StrOutputParser()
            response = chain.invoke({'context': context, 'question': query})
            
            # Enviar resposta
            self.output_queue.put(('__BOT__', f'\n🤖 Resposta:\n{response}\n'))
            
            # Citar fontes de forma mais compacta
            if relevant_docs:
                self.output_queue.put(('__SOURCE_HEADER__', '\n📚 Fontes:\n'))
                for idx, doc in enumerate(relevant_docs, 1):
                    source = doc.metadata.get('source', 'Fonte desconhecida')
                    # Extrair apenas o nome do arquivo
                    import os
                    source_name = os.path.basename(source)
                    page = doc.metadata.get('page', '')
                    page_info = f' (pág. {page + 1})' if page != '' else ''
                    
                    fonte_msg = f'  [{idx}] {source_name}{page_info}\n'
                    self.output_queue.put(('__SOURCE_ITEM__', fonte_msg))
        except Exception as e:
            self.output_queue.put(('__BOT__', f'\n❌ Erro: {str(e)}\n\n'))
        finally:
            self.processing = False
            self.output_queue.put('__SHOW_PROMPT__')
            
    def check_queue(self):
        try:
            while True:
                message = self.output_queue.get_nowait()
                if message == '__SHOW_PROMPT__':
                    self.show_prompt()
                elif isinstance(message, tuple) and len(message) == 2:
                    # Mensagem com tag de cor específica (tag, texto)
                    tag, text = message
                    if tag == '__SOURCE_HEADER__':
                        self.write_to_terminal(text, color_tag='source_color')
                    elif tag == '__SOURCE_ITEM__':
                        self.write_to_terminal(text, color_tag='source_color')
                    elif tag == '__BOT__':
                        self.write_to_terminal(text, color_tag='bot_color')
                    elif tag == '__USER__':
                        self.write_to_terminal(text, color_tag='user_color')
                    else:
                        self.write_to_terminal(text, color_tag='bot_color')
                else:
                    # Mensagem simples - assumir que é do bot
                    self.write_to_terminal(message, color_tag='bot_color')
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)

def main():
    root = tk.Tk()
    app = ChatbotRAGGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
