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
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

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
        self.setup_style()
        self.create_widgets()
        self.check_queue()
        
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
        
        ttk.Button(btn_frame, text='Adicionar PDF', command=self.add_pdf).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Listar Arquivos', command=self.list_files).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Ajuda', command=self.show_help).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(btn_frame, text='Limpar', command=self.clear_terminal).pack(side=tk.RIGHT)
        
        term_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        term_frame.pack(fill=tk.BOTH, expand=True)
        
        # Terminal com input integrado
        self.terminal_output = scrolledtext.ScrolledText(
            term_frame, 
            height=20, 
            bg='#1e1e1e', 
            fg='#00ff00', 
            font=('Consolas', 10), 
            wrap=tk.WORD,
            insertbackground='#00ff00'  # Cor do cursor
        )
        self.terminal_output.pack(fill=tk.BOTH, expand=True)
        
        # Bind de teclas para o terminal
        self.terminal_output.bind('<Return>', self.handle_input)
        self.terminal_output.bind('<KeyPress>', self.on_key_press)
        
        # Variável para rastrear a linha de input
        self.input_start = '1.0'
        self.processing = False
        
        self.write_to_terminal('Bem-vindo ao Chatbot RAG!\n')
        self.write_to_terminal('Digite sua pergunta e pressione Enter.\n\n')
        self.show_prompt()
        
    def write_to_terminal(self, text, bot=True):
        self.terminal_output.insert(tk.END, text)
        self.terminal_output.see(tk.END)
        
    def show_prompt(self):
        """Mostra o prompt de comando"""
        if not self.processing:
            self.terminal_output.insert(tk.END, '> ')
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
            self.terminal_output.insert(tk.END, '\n')
            self.processing = True
            threading.Thread(target=self._chat_worker, args=(user_input,), daemon=True).start()
        else:
            self.terminal_output.insert(tk.END, '\n')
            self.show_prompt()
        
        return 'break'  # Impede a quebra de linha padrão
        
    def clear_terminal(self):
        self.terminal_output.delete(1.0, tk.END)
        self.write_to_terminal('Terminal limpo!\n\n')
        self.processing = False
        self.show_prompt()
        
    def add_pdf(self):
        file_path = filedialog.askopenfilename(title='Selecione PDF', filetypes=[('PDF', '*.pdf')])
        if file_path:
            self.write_to_terminal(f'\nAdicionando {file_path}...\n')
            threading.Thread(target=self._add_pdf_worker, args=(file_path,), daemon=True).start()
            
    def _add_pdf_worker(self, file_path):
        try:
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
            chunks = splitter.split_documents(docs)
            embeddings = OllamaEmbeddings(model=EMBED_MODEL)
            Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=DB_PATH)
            self.output_queue.put('Arquivo adicionado com sucesso!\n\n')
        except Exception as e:
            self.output_queue.put(f'Erro: {str(e)}\n\n')
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
            
    def show_help(self):
        self.write_to_terminal('\n=== AJUDA ===\n')
        self.write_to_terminal('1. Clique em "Adicionar PDF" para carregar documentos\n')
        self.write_to_terminal('2. Digite sua pergunta após o prompt >\n')
        self.write_to_terminal('3. Pressione Enter para enviar\n')
        self.write_to_terminal('4. Use "Listar Arquivos" para ver PDFs adicionados\n\n')
        self.show_prompt()
    
    def list_files(self):
        self.write_to_terminal('\nListando arquivos no armazem...\n')
        threading.Thread(target=self._list_files_worker, daemon=True).start()
    
    def _list_files_worker(self):
        try:
            import os
            if not os.path.exists(DB_PATH):
                self.output_queue.put('Armazem ainda nao foi criado. Adicione um PDF primeiro.\n\n')
                return
            
            embeddings = OllamaEmbeddings(model=EMBED_MODEL)
            db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
            
            try:
                all_docs = db.get()
            except Exception:
                self.output_queue.put('Armazem esta vazio. Adicione um PDF primeiro.\n\n')
                return
            
            if not all_docs or not all_docs.get('metadatas'):
                self.output_queue.put('Armazem esta vazio.\n\n')
                return
            
            sources = set(meta['source'] for meta in all_docs['metadatas'] if 'source' in meta)
            
            if not sources:
                self.output_queue.put('Nenhum arquivo encontrado.\n\n')
                return
            
            self.output_queue.put('\n=== Arquivos no armazem ===\n')
            for idx, source in enumerate(sorted(sources), 1):
                self.output_queue.put(f'{idx}. {source}\n')
            self.output_queue.put('\n')
        except Exception as e:
            import traceback
            error_msg = f'Erro ao listar arquivos: {str(e)}\n'
            self.output_queue.put(error_msg + '\n')
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
            
    def _chat_worker(self, query):
        try:
            self.output_queue.put('Processando...\n')
            embeddings = OllamaEmbeddings(model=EMBED_MODEL)
            db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
            retriever = db.as_retriever(search_kwargs={'k': 4})
            llm = Ollama(model=LLM_MODEL)
            template = 'Responda baseado no contexto:\n\nContexto: {context}\n\nPergunta: {question}\n\nResposta:'
            prompt = ChatPromptTemplate.from_template(template)
            def format_docs(docs):
                return '\n\n'.join(doc.page_content for doc in docs)
            rag_chain = ({'context': retriever | format_docs, 'question': RunnablePassthrough()} | prompt | llm | StrOutputParser())
            response = rag_chain.invoke(query)
            self.output_queue.put(f'\n{response}\n\n')
        except Exception as e:
            self.output_queue.put(f'\nErro: {str(e)}\n\n')
        finally:
            self.processing = False
            self.output_queue.put('__SHOW_PROMPT__')
            
    def check_queue(self):
        try:
            while True:
                message = self.output_queue.get_nowait()
                if message == '__SHOW_PROMPT__':
                    self.show_prompt()
                else:
                    self.write_to_terminal(message)
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
