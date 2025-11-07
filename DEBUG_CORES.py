"""
Script de Debug - Intercepta TODAS as mensagens da fila
Execute este ao invés do main.py para ver o que está acontecendo
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import threading
import queue
import os
import sys

# Desabilitar telemetria
os.environ['ANONYMIZED_TELEMETRY'] = 'False'
os.environ['CHROMA_TELEMETRY'] = 'False'

# Patches chromadb
try:
    import chromadb.telemetry.product.posthog
except:
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

try:
    import chromadb.api.rust
except:
    import types
    import chromadb
    if not hasattr(chromadb, 'api'):
        chromadb.api = types.ModuleType('api')
    if not hasattr(chromadb.api, 'rust'):
        chromadb.api.rust = types.ModuleType('rust')
    sys.modules['chromadb.api'] = chromadb.api
    sys.modules['chromadb.api.rust'] = chromadb.api.rust

from langchain_community.llms import Ollama
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

try:
    from sentence_transformers import CrossEncoder
    RERANK_SUPPORT = True
except ImportError:
    RERANK_SUPPORT = False

DB_PATH = './meu_armazem_chroma'
EMBED_MODEL = 'nomic-embed-text'
LLM_MODEL = 'deepseek-r1:8b'

class ChatbotRAGGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('DEBUG - Chatbot RAG')
        self.root.geometry('1000x700')
        self.root.configure(bg='#2b2b2b')
        
        self.output_queue = queue.Queue()
        self.processing = False
        
        self.llm = None
        self.embeddings = None
        self.db = None
        self.rag_chain = None
        self.reranker = None
        
        self.setup_style()
        self.create_widgets()
        self.check_queue()
        
        # Mensagem inicial SEMPRE via fila
        print("DEBUG: Enviando mensagem inicial para fila")
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
        
        title = ttk.Label(main_frame, text='DEBUG - Chatbot RAG', style='Dark.TLabel')
        title.pack(pady=(0, 10))
        
        btn_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(btn_frame, text='Teste Verde', command=lambda: self.test_color('__BOT__', 'Texto VERDE\n')).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text='Teste Azul', command=lambda: self.test_color('__USER__', 'Texto AZUL\n')).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text='Teste Laranja', command=lambda: self.test_color('__SOURCE__', 'Texto LARANJA\n')).pack(side=tk.LEFT, padx=5)
        
        term_frame = ttk.Frame(main_frame, style='Dark.TFrame')
        term_frame.pack(fill=tk.BOTH, expand=True)
        
        # Terminal
        self.terminal_output = scrolledtext.ScrolledText(
            term_frame, 
            height=20, 
            bg='#1e1e1e', 
            fg='#00ff00',
            font=('Courier New', 10),
            wrap=tk.WORD,
            insertbackground='#00ff00',
            state='normal'
        )
        self.terminal_output.pack(fill=tk.BOTH, expand=True)
        
        # Tags
        print("DEBUG: Configurando tags de cores")
        self.terminal_output.tag_configure('bot_color', foreground='#00ff00')
        self.terminal_output.tag_configure('user_color', foreground='#00bfff')
        self.terminal_output.tag_configure('source_color', foreground='#ffa500')
        self.terminal_output.tag_configure('prompt_color', foreground='#ffffff')
        
        self.input_start = '1.0'
        
        # Mensagens de boas-vindas
        print("DEBUG: Enviando mensagens de boas-vindas")
        self.output_queue.put(('__BOT__', 'Bem-vindo ao Chatbot RAG!\n'))
        self.output_queue.put(('__BOT__', 'Digite sua pergunta e pressione Enter.\n\n'))
        self.output_queue.put('__SHOW_PROMPT__')
        
    def test_color(self, tag, text):
        """Testa cores diretamente"""
        print(f"DEBUG: Testando cor - Tag: {tag}, Text: {text.strip()}")
        self.output_queue.put((tag, text))
        
    def write_to_terminal(self, text, bot=True, color_tag=None):
        """Escreve no terminal com cor apropriada"""
        start_idx = self.terminal_output.index("end-1c")
        self.terminal_output.insert(tk.END, text)
        end_idx = self.terminal_output.index("end-1c")
        
        if color_tag:
            print(f"DEBUG: Aplicando tag '{color_tag}' de {start_idx} a {end_idx}")
            self.terminal_output.tag_add(color_tag, start_idx, end_idx)
            
            # Verificar se a tag foi aplicada
            tags_applied = self.terminal_output.tag_names(start_idx)
            print(f"DEBUG: Tags aplicadas em {start_idx}: {tags_applied}")
        else:
            print(f"DEBUG: NENHUMA TAG especificada para texto: {text[:30]}")
        
        self.terminal_output.see(tk.END)
        
    def show_prompt(self):
        """Mostra o prompt"""
        if not self.processing:
            start_pos = self.terminal_output.index(tk.END)
            self.terminal_output.insert(tk.END, '\n> ')
            end_pos = self.terminal_output.index(tk.END)
            self.terminal_output.tag_add('prompt_color', start_pos, end_pos)
            self.terminal_output.see(tk.END)
            self.input_start = self.terminal_output.index(tk.END + '-1c')
            
    def initialize_components(self):
        """Inicializa componentes"""
        try:
            self.embeddings = OllamaEmbeddings(model=EMBED_MODEL)
            self.db = Chroma(persist_directory=DB_PATH, embedding_function=self.embeddings)
            self.llm = Ollama(model=LLM_MODEL)
            
            if RERANK_SUPPORT:
                self.output_queue.put(('__BOT__', '📊 Carregando modelo de re-ranking...\n'))
                self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
                self.output_queue.put(('__BOT__', '✅ Re-ranking habilitado!\n'))
            
            self.output_queue.put(('__BOT__', '✅ Modelos prontos para uso!\n'))
        except Exception as e:
            self.output_queue.put(('__BOT__', f'❌ Erro: {e}\n'))
        finally:
            self.output_queue.put('__SHOW_PROMPT__')
            
    def check_queue(self):
        try:
            while True:
                message = self.output_queue.get_nowait()
                print(f"DEBUG: Mensagem da fila: {message}")
                
                if message == '__SHOW_PROMPT__':
                    print("DEBUG: Mostrando prompt")
                    self.show_prompt()
                elif isinstance(message, tuple) and len(message) == 2:
                    tag, text = message
                    print(f"DEBUG: Tupla recebida - Tag: {tag}, Text: {text[:50]}")
                    
                    if tag == '__SOURCE_HEADER__' or tag == '__SOURCE__':
                        self.write_to_terminal(text, color_tag='source_color')
                    elif tag == '__SOURCE_ITEM__':
                        self.write_to_terminal(text, color_tag='source_color')
                    elif tag == '__BOT__':
                        self.write_to_terminal(text, color_tag='bot_color')
                    elif tag == '__USER__':
                        self.write_to_terminal(text, color_tag='user_color')
                    else:
                        print(f"DEBUG: Tag desconhecida: {tag}")
                        self.write_to_terminal(text, color_tag='bot_color')
                else:
                    print(f"DEBUG: Mensagem simples (não tupla): {message}")
                    self.write_to_terminal(message, color_tag='bot_color')
        except queue.Empty:
            pass
        finally:
            self.root.after(100, self.check_queue)

def main():
    print("DEBUG: Iniciando aplicação")
    root = tk.Tk()
    app = ChatbotRAGGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
