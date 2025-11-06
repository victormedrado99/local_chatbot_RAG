# 🤖 Chatbot RAG - Sistema de IA com Documentos PDF# 🤖 Chatbot RAG - Interface Gráfica



Sistema de chatbot inteligente que responde perguntas baseado em documentos PDF usando RAG (Retrieval-Augmented Generation) com interface gráfica.Sistema de chatbot com IA que responde perguntas baseado em documentos PDF usando interface gráfica.



## 📋 Pré-requisitos## 🎯 Características



### 1. Python- **Interface Gráfica Moderna**: GUI com tkinter em modo escuro

- **Versão**: Python 3.8 ou superior- **Terminal Integrado**: Terminal exclusivo para interação com o chatbot

- Verifique sua versão: `python --version`- **Adicionar PDFs**: Botão dedicado para selecionar e adicionar arquivos PDF

- **Chat em Tempo Real**: Campo de entrada para fazer perguntas aos documentos

### 2. Ollama- **Threading**: Operações executadas em threads separadas para não travar a interface

O Ollama é necessário para executar os modelos de IA localmente.

## 🚀 Como Usar

#### Instalação do Ollama:

1. Acesse: https://ollama.ai/download### 1. Executar a Aplicação

2. Baixe e instale o Ollama para Windows```bash

3. Verifique a instalação: `ollama --version`python main.py

```

#### Baixar os Modelos Necessários:

Após instalar o Ollama, execute os seguintes comandos:### 2. Interface Principal



```bashA aplicação abrirá uma janela com:

# Modelo de embeddings (para vetorização de documentos)

ollama pull nomic-embed-text#### 📊 Botões Principais:

- **📄 Adicionar PDF**: Abre um diálogo para selecionar arquivos PDF

# Modelo de linguagem (para geração de respostas)- **📁 Listar Arquivos**: Mostra todos os PDFs adicionados ao armazém

ollama pull deepseek-r1:8b- **🗑️ Limpar Terminal**: Limpa o terminal integrado

```

#### 💻 Terminal Integrado:

**Nota**: O download dos modelos pode levar alguns minutos dependendo da sua conexão.- Mostra todas as operações e respostas do sistema

- Interface de console em modo escuro

#### Verificar se o Ollama está rodando:- Scroll automático para acompanhar as mensagens

```bash

ollama list#### 💬 Campo de Chat:

```- Digite suas perguntas no campo inferior

Você deve ver os modelos `nomic-embed-text` e `deepseek-r1:8b` listados.- Pressione **Enter** ou clique em **📤 Enviar**

- O chatbot responderá baseado nos documentos adicionados

## 🚀 Instalação do Projeto

## 🔧 Funcionalidades

### 1. Clone ou baixe o repositório

```bash### Adicionar Documentos PDF

git clone https://github.com/victormedrado99/local_chatbot_RAG.git1. Clique em **📄 Adicionar PDF**

cd local_chatbot_RAG2. Selecione um ou mais arquivos PDF

```3. O sistema processará e adicionará ao armazém automaticamente

4. Uma mensagem de confirmação aparecerá no terminal

### 2. Crie um ambiente virtual (recomendado)

```bash### Fazer Perguntas

python -m venv .venv1. Digite sua pergunta no campo inferior

```2. Pressione Enter ou clique em **📤 Enviar**

3. O sistema buscará informações relevantes nos documentos

### 3. Ative o ambiente virtual4. A resposta aparecerá no terminal



**Windows (PowerShell):**### Listar Documentos

```powershell1. Clique em **📁 Listar Arquivos**

.venv\Scripts\activate2. O terminal mostrará todos os PDFs no armazém

```

## ⚙️ Configurações

**Windows (CMD):**

```cmd### Modelos Configurados:

.venv\Scripts\activate.bat- **LLM**: `deepseek-r1:8b` (via Ollama)

```- **Embeddings**: `nomic-embed-text`

- **Banco Vetorial**: ChromaDB (persistente)

**Linux/Mac:**

```bash### Diretório de Dados:

source .venv/bin/activate- **Armazém**: `./meu_armazem_chroma`

```

## 🎨 Interface

### 4. Instale as dependências

```bash### Design:

pip install langchain langchain-community langchain-core langchain-chroma langchain-ollama chromadb pymupdf- **Tema**: Modo escuro moderno

```- **Cores**: Cinza escuro com texto branco

- **Fonte**: Consolas para terminal, Arial para interface

## 🎯 Como Usar- **Emojis**: Interface amigável com ícones visuais



### 1. Certifique-se que o Ollama está rodando### Layout:

O Ollama deve estar em execução em segundo plano. Normalmente ele inicia automaticamente após a instalação.```

┌─────────────────────────────────────────────────┐

Para iniciar manualmente (se necessário):│          🤖 Chatbot RAG - IA com Documentos     │

```bash├─────────────────────────────────────────────────┤

ollama serve│ [📄 Adicionar PDF] [📁 Listar] [🗑️ Limpar]    │

```├─────────────────────────────────────────────────┤

│                                                 │

### 2. Execute o programa│               💻 Terminal                       │

```bash│  ┌─────────────────────────────────────────┐    │

python main.py│  │ Saída do sistema aqui...                │    │

```│  │                                         │    │

│  │                                         │    │

Ou, se estiver usando ambiente virtual:│  └─────────────────────────────────────────┘    │

```bash│                                                 │

.venv\Scripts\python.exe main.py│ 💬 Pergunta: [_______________] [📤 Enviar]     │

```└─────────────────────────────────────────────────┘

```

### 3. Interface do Chatbot

## 🛠️ Tecnologias Utilizadas

A janela do chatbot abrirá com os seguintes botões:

- **Python 3.8+**

- **📄 Adicionar PDF**: Clique para selecionar e adicionar documentos PDF ao armazém- **Tkinter**: Interface gráfica

- **📁 Listar Arquivos**: Mostra todos os PDFs que foram adicionados- **LangChain**: Framework para IA e RAG

- **❓ Ajuda**: Exibe instruções de uso no terminal- **ChromaDB**: Banco de dados vetorial

- **🗑️ Limpar**: Limpa o terminal de chat- **Ollama**: Servidor de LLM local

- **PyMuPDF**: Processamento de PDFs

### 4. Workflow de Uso

## 📝 Dependências

1. **Adicione documentos PDF**:

   - Clique em "Adicionar PDF"Instale as dependências necessárias:

   - Selecione um arquivo PDF do seu computador

   - Aguarde a confirmação: "Arquivo adicionado com sucesso!"```bash

pip install langchain langchain-community langchain-core langchain-chroma chromadb pymupdf

2. **Faça perguntas**:```

   - Digite sua pergunta no campo de entrada na parte inferior

   - Pressione Enter ou clique em "Enviar"## 🚀 Inicialização Rápida

   - O bot processará e responderá baseado nos documentos

1. **Clone ou baixe o projeto**

3. **Liste os arquivos** (opcional):2. **Instale as dependências**

   - Clique em "Listar Arquivos" para ver todos os PDFs adicionados3. **Certifique-se que o Ollama está rodando com o modelo deepseek-r1:8b**

4. **Execute**: `python main.py`

## ⚙️ Configuração5. **Adicione seus PDFs e comece a conversar!**



### Modelos Configurados---

Os modelos podem ser alterados no arquivo `main.py`:

> **Nota**: Este sistema requer que o Ollama esteja rodando localmente com os modelos `deepseek-r1:8b` e `nomic-embed-text` instalados.
```python
DB_PATH = './meu_armazem_chroma'  # Diretório do banco vetorial
EMBED_MODEL = 'nomic-embed-text'   # Modelo de embeddings
LLM_MODEL = 'deepseek-r1:8b'       # Modelo de linguagem
```

### Modelos Alternativos no Ollama
Você pode usar outros modelos disponíveis no Ollama:

**Para o LLM (geração de respostas):**
- `llama3`
- `mistral`
- `gemma`
- `phi3`

Para trocar, baixe o modelo e altere `LLM_MODEL` no código:
```bash
ollama pull llama3
```

## 🗂️ Estrutura do Projeto

```
local_chatbot_RAG/
├── main.py                    # Código principal da aplicação
├── README.md                  # Este arquivo
├── .gitignore                 # Arquivos ignorados pelo Git
├── .venv/                     # Ambiente virtual (após criação)
└── meu_armazem_chroma/        # Banco de dados vetorial (criado automaticamente)
```

## 🔧 Troubleshooting

### Erro: "No module named 'langchain_ollama'"
**Solução**: Instale o pacote:
```bash
pip install langchain-ollama
```

### Erro: "model 'nomic-embed-text' not found"
**Solução**: Baixe o modelo de embeddings:
```bash
ollama pull nomic-embed-text
```

### Erro: "model 'deepseek-r1:8b' not found"
**Solução**: Baixe o modelo de linguagem:
```bash
ollama pull deepseek-r1:8b
```

### Erro: "Connection refused" ao adicionar PDF
**Solução**: Certifique-se que o Ollama está rodando:
```bash
ollama serve
```

### Programa não abre a janela
**Solução**: Verifique se o tkinter está instalado:
```bash
python -m tkinter
```
Se não funcionar, reinstale o Python com suporte a tkinter.

## 📊 Requisitos de Sistema

- **RAM**: Mínimo 8GB (recomendado 16GB para modelos maiores)
- **Armazenamento**: ~5GB para os modelos
- **Sistema Operacional**: Windows 10/11, Linux, macOS
- **Conexão**: Necessária apenas para download inicial dos modelos

## 🛡️ Privacidade

- ✅ Todos os dados são processados **localmente**
- ✅ Nenhuma informação é enviada para servidores externos
- ✅ Seus documentos ficam apenas no seu computador

## 🎨 Interface

### Design:
- **Tema**: Modo escuro moderno
- **Terminal integrado**: Para interação e visualização de respostas
- **Botões intuitivos**: Fácil navegação

### Layout:
```
┌─────────────────────────────────────────────────┐
│          🤖 Chatbot RAG                         │
├─────────────────────────────────────────────────┤
│ [📄 PDF] [📁 Listar] [❓ Ajuda] [🗑️ Limpar]    │
├─────────────────────────────────────────────────┤
│                                                 │
│               💻 Terminal Chat                  │
│  ┌─────────────────────────────────────────┐    │
│  │ Bot: Bem-vindo ao Chatbot RAG!          │    │
│  │                                         │    │
│  │                                         │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
│ [_______________entrada_______________] [Enviar]│
└─────────────────────────────────────────────────┘
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Tkinter**: Interface gráfica
- **LangChain**: Framework para IA e RAG
- **ChromaDB**: Banco de dados vetorial
- **Ollama**: Servidor de LLM local
- **PyMuPDF**: Processamento de PDFs

## 📝 Licença

Este projeto está sob a licença MIT.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📧 Contato

- GitHub: [@victormedrado99](https://github.com/victormedrado99)
- Repositório: [local_chatbot_RAG](https://github.com/victormedrado99/local_chatbot_RAG)

---

**Desenvolvido com ❤️ usando Python, LangChain e Ollama**
