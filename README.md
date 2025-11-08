# 🕹️ Chatbot RAG v1.0 - Terminal Retro Edition# 🕹️ Chatbot RAG v1.0 - Terminal Retro Edition



Sistema de chatbot inteligente com **visual retro anos 90** que responde perguntas baseadas em documentos PDF usando **RAG (Retrieval-Augmented Generation)** avançado com **re-ranking** e **streaming de respostas**.Sistema de chatbot inteligente com **visual retro anos 90** que responde perguntas baseadas em documentos PDF usando **RAG (Retrieval-Augmented Generation)** avançado com **re-ranking** e **streaming de respostas**.



```

╔════════════════════════════════════════════════╗

║  CHATBOT RAG v1.0 - TERMINAL RETRO EDITION    ║

║  (C) 2025 - RAG TERMINAL SYSTEMS               ║## 🎯 Características Principais

╚════════════════════════════════════════════════╝

```### 🚀 **RAG Avançado com Re-Ranking**

- **Cross-Encoder Re-Ranking**: Usa modelo `ms-marco-MiniLM-L-6-v2` para reordenar resultados

---- **Busca em 2 Etapas**: Fetch 10 documentos → Score com cross-encoder → Seleciona top 4

- **Precisão Aumentada**: 30-40% melhor relevância vs busca por embeddings pura

## 🎯 Características Principais

### ⚡ **Streaming de Respostas em Tempo Real**

### 🚀 **RAG Avançado com Re-Ranking**- **Output Palavra-por-Palavra**: Respostas aparecem enquanto são geradas

- **Cross-Encoder Re-Ranking**: Usa modelo `ms-marco-MiniLM-L-6-v2` para reordenar resultados- **Feedback Instantâneo**: Veja o bot "pensando" em tempo real

- **Busca em 2 Etapas**: Fetch 10 documentos → Score com cross-encoder → Seleciona top 4- **Performance Percebida**: Interface mais responsiva e dinâmica

- **Precisão Aumentada**: 30-40% melhor relevância vs busca por embeddings pura

### 📚 **Citações de Fontes Inteligentes**

### ⚡ **Streaming de Respostas em Tempo Real**- **Snippets Contextuais**: 200 caracteres de contexto por fonte

- **Output Palavra-por-Palavra**: Respostas aparecem enquanto são geradas- **Truncamento Inteligente**: Quebra em limites de palavras, não no meio

- **Feedback Instantâneo**: Veja o bot "pensando" em tempo real- **Rastreabilidade**: Nome do arquivo, página e trecho exato citado

- **Performance Percebida**: Interface mais responsiva e dinâmica

### 🎨 **Visual Retro Terminal Anos 90**

### 📚 **Citações de Fontes Inteligentes**- **Estética CRT**: Monitor fosforescente verde sobre fundo preto

- **Snippets Contextuais**: 200 caracteres de contexto por fonte- **ASCII Art**: Bordas e títulos estilo DOS/Unix

- **Truncamento Inteligente**: Quebra em limites de palavras, não no meio- **Cores Neon**: Verde (#00ff00), Ciano (#00ffff), Amarelo (#ffff00)

- **Rastreabilidade**: Nome do arquivo, página e trecho exato citado- **Mensagens Terminal**: Sistema com prefixos `>>>` estilo command-line

- **Botões Retro**: Estilo DOS com prefixos `[SÍMBOLO]`

### 🎨 **Visual Retro Terminal Anos 90**- **Cursor Largo**: 8px tipo DOS piscante

- **Estética CRT**: Monitor fosforescente verde sobre fundo preto

- **ASCII Art**: Bordas e títulos estilo DOS/Unix### 💻 **Interface Gráfica Completa**

- **Cores Neon**: Verde (#00ff00), Ciano (#00ffff), Amarelo (#ffff00)- **Tkinter Modern**: GUI com tema retro escuro

- **Mensagens Terminal**: Sistema com prefixos `>>>` estilo command-line- **Terminal Integrado**: Output estilo console com cores diferenciadas

- **Botões Retro**: Estilo DOS com prefixos `[SÍMBOLO]`- **Operações Assíncronas**: Threading para não travar a interface

- **Cursor Largo**: 8px tipo DOS piscante- **Feedback Visual**: Status de carregamento e processamento



### 💻 **Interface Gráfica Completa**### 🔒 **100% Local e Privado**

- **Tkinter Modern**: GUI com tema retro escuro- **Sem Internet**: Tudo roda localmente após setup inicial

- **Terminal Integrado**: Output estilo console com cores diferenciadas- **Privacidade Total**: Seus documentos nunca saem do seu computador

- **Operações Assíncronas**: Threading para não travar a interface- **Ollama Local**: LLM e embeddings rodando na sua máquina

- **Feedback Visual**: Status de carregamento e processamento



### 🔒 **100% Local e Privado**

- **Sem Internet**: Tudo roda localmente após setup inicialO Ollama é necessário para executar os modelos de IA localmente.

- **Privacidade Total**: Seus documentos nunca saem do seu computador

- **Ollama Local**: LLM e embeddings rodando na sua máquina## 🚀 Como Usar



---#### Instalação do Ollama:



## 📋 Pré-requisitos1. Acesse: https://ollama.ai/download### 1. Executar a Aplicação



### 1. **Python 3.8+**2. Baixe e instale o Ollama para Windows```bash

Verifique sua versão:

```bash3. Verifique a instalação: `ollama --version`python main.py

python --version

``````



### 2. **Ollama** (Servidor LLM Local)#### Baixar os Modelos Necessários:



#### Instalação:Após instalar o Ollama, execute os seguintes comandos:### 2. Interface Principal

1. Acesse: https://ollama.ai/download

2. Baixe e instale para Windows

3. Verifique: `ollama --version`

```bashA aplicação abrirá uma janela com:

#### Modelos Necessários:

```bash# Modelo de embeddings (para vetorização de documentos)

# Embeddings (vetorização de documentos)

ollama pull nomic-embed-textollama pull nomic-embed-text#### 📊 Botões Principais:



# LLM (geração de respostas)- **📄 Adicionar PDF**: Abre um diálogo para selecionar arquivos PDF

ollama pull deepseek-r1:8b

```# Modelo de linguagem (para geração de respostas)- **📁 Listar Arquivos**: Mostra todos os PDFs adicionados ao armazém



**Nota**: Download dos modelos ~5GB, pode demorar alguns minutos.ollama pull deepseek-r1:8b- **🗑️ Limpar Terminal**: Limpa o terminal integrado



#### Verificar Instalação:```

```bash

ollama list#### 💻 Terminal Integrado:

```

Você deve ver `nomic-embed-text` e `deepseek-r1:8b` listados.**Nota**: O download dos modelos pode levar alguns minutos dependendo da sua conexão.- Mostra todas as operações e respostas do sistema



---- Interface de console em modo escuro



## 🚀 Instalação Rápida#### Verificar se o Ollama está rodando:- Scroll automático para acompanhar as mensagens



### 1. Clone o Repositório```bash

```bash

git clone https://github.com/victormedrado99/local_chatbot_RAG.gitollama list#### 💬 Campo de Chat:

cd local_chatbot_RAG

``````- Digite suas perguntas no campo inferior



### 2. Crie Ambiente Virtual (Recomendado)Você deve ver os modelos `nomic-embed-text` e `deepseek-r1:8b` listados.- Pressione **Enter** ou clique em **📤 Enviar**

```bash

python -m venv .venv- O chatbot responderá baseado nos documentos adicionados

```

## 🚀 Instalação do Projeto

### 3. Ative o Ambiente Virtual

## 🔧 Funcionalidades

**Windows (PowerShell):**

```powershell### 1. Clone ou baixe o repositório

.venv\Scripts\activate

``````bash### Adicionar Documentos PDF



**Windows (CMD):**git clone https://github.com/victormedrado99/local_chatbot_RAG.git1. Clique em **📄 Adicionar PDF**

```cmd

.venv\Scripts\activate.batcd local_chatbot_RAG2. Selecione um ou mais arquivos PDF

```

```3. O sistema processará e adicionará ao armazém automaticamente

**Linux/Mac:**

```bash4. Uma mensagem de confirmação aparecerá no terminal

source .venv/bin/activate

```### 2. Crie um ambiente virtual (recomendado)



### 4. Instale Dependências```bash### Fazer Perguntas

```bash

pip install langchain langchain-community langchain-core langchain-chroma langchain-ollama chromadb pymupdf sentence-transformerspython -m venv .venv1. Digite sua pergunta no campo inferior

```

```2. Pressione Enter ou clique em **📤 Enviar**

### 5. Execute o Chatbot

```bash3. O sistema buscará informações relevantes nos documentos

python main.py

```### 3. Ative o ambiente virtual4. A resposta aparecerá no terminal



---



## 💻 Como Usar**Windows (PowerShell):**### Listar Documentos



### Interface Retro Terminal```powershell1. Clique em **📁 Listar Arquivos**



Ao executar `python main.py`, você verá:.venv\Scripts\activate2. O terminal mostrará todos os PDFs no armazém



``````

╔════════════════════════════════════════════════╗

║  CHATBOT RAG v1.0 - SISTEMA INICIALIZADO      ║## ⚙️ Configurações

║  (C) 2025 - RAG TERMINAL SYSTEMS               ║

╚════════════════════════════════════════════════╝**Windows (CMD):**



Digite sua pergunta no prompt e pressione ENTER.```cmd### Modelos Configurados:

Digite [?] HELP para ver comandos disponíveis.

.venv\Scripts\activate.bat- **LLM**: `deepseek-r1:8b` (via Ollama)

>>> CARREGANDO MODELOS DE IA...

>>> LOADING: Cross-Encoder Re-Ranking Module...```- **Embeddings**: `nomic-embed-text`

>>> STATUS: Re-ranking [ENABLED]

- **Banco Vetorial**: ChromaDB (persistente)

>>> SYSTEM READY - All models loaded successfully!

>>> Type your query below:**Linux/Mac:**



> _```bash### Diretório de Dados:

```

source .venv/bin/activate- **Armazém**: `./meu_armazem_chroma`

### Botões Disponíveis

```

```

[+] ADD DOC    - Adicionar documentos PDF## 🎨 Interface

[≡] LIST       - Listar todos os PDFs no armazém

[-] REMOVE     - Remover documentos do banco### 4. Instale as dependências

[?] HELP       - Exibir ajuda e comandos

[X] CLEAR      - Limpar terminal```bash### Design:

```

pip install langchain langchain-community langchain-core langchain-chroma langchain-ollama chromadb pymupdf- **Tema**: Modo escuro moderno

### Workflow de Uso

```- **Cores**: Cinza escuro com texto branco

1. **Adicione Documentos PDF**:

   - Clique em `[+] ADD DOC`- **Fonte**: Consolas para terminal, Arial para interface

   - Selecione um ou mais arquivos PDF

   - Aguarde processamento: `>>> LOADING: Processing PDF...`## 🎯 Como Usar- **Emojis**: Interface amigável com ícones visuais

   - Confirmação: `>>> STATUS: Document added successfully!`



2. **Faça Perguntas**:

   - Digite no prompt: `> sua pergunta aqui`### 1. Certifique-se que o Ollama está rodando### Layout:

   - Pressione **Enter**

   - Veja processamento: `>>> PROCESSING QUERY...`O Ollama deve estar em execução em segundo plano. Normalmente ele inicia automaticamente após a instalação.```



3. **Receba Resposta com Streaming**:┌─────────────────────────────────────────────────┐

   ```

   >>> OUTPUT:Para iniciar manualmente (se necessário):│          🤖 Chatbot RAG - IA com Documentos     │

   ────────────────────────────────────────────────

   Sua resposta aparece palavra por palavra em```bash├─────────────────────────────────────────────────┤

   tempo real, simulando um terminal processando...

   ────────────────────────────────────────────────ollama serve│ [📄 Adicionar PDF] [📁 Listar] [🗑️ Limpar]    │

   ```

```├─────────────────────────────────────────────────┤

4. **Veja Fontes com Contexto**:

   ```│                                                 │

   >>> SOURCES REFERENCED:

   ### 2. Execute o programa│               💻 Terminal                       │

     [1] Documento.pdf (pág. 5)

         "...trecho de 200 caracteres do documento```bash│  ┌─────────────────────────────────────────┐    │

         mostrando o contexto exato da citação..."

   python main.py│  │ Saída do sistema aqui...                │    │

     [2] Outro_Doc.pdf (pág. 12)

         "...mais contexto relevante da fonte..."```│  │                                         │    │

   ```

│  │                                         │    │

---

Ou, se estiver usando ambiente virtual:│  └─────────────────────────────────────────┘    │

## 🎨 Visual Retro Anos 90

```bash│                                                 │

### Paleta de Cores

.venv\Scripts\python.exe main.py│ 💬 Pergunta: [_______________] [📤 Enviar]     │

| Elemento | Cor | Hex | Inspiração |

|----------|-----|-----|------------|```└─────────────────────────────────────────────────┘

| **Bot** | Verde Neon | `#00ff00` | Terminais Unix/DOS |

| **Usuário** | Ciano | `#00ffff` | IBM PC, MS-DOS |```

| **Fontes** | Amarelo | `#ffff00` | Avisos DOS/BIOS |

| **Prompt** | Branco | `#ffffff` | Cursor padrão |### 3. Interface do Chatbot

| **Fundo** | Preto Total | `#000000` | Monitor CRT |

## 🛠️ Tecnologias Utilizadas

### Elementos Visuais

A janela do chatbot abrirá com os seguintes botões:

- **ASCII Art Borders**: `╔═══╗` `║   ║` `╚═══╝`

- **Separadores**: `────────────────────`- **Python 3.8+**

- **Prefixos Terminal**: `>>>` `> `

- **Botões DOS**: `[SÍMBOLO]` estilo- **📄 Adicionar PDF**: Clique para selecionar e adicionar documentos PDF ao armazém- **Tkinter**: Interface gráfica

- **Fonte**: Courier New Bold (monoespaçada)

- **Cursor**: 8px largo tipo DOS- **📁 Listar Arquivos**: Mostra todos os PDFs que foram adicionados- **LangChain**: Framework para IA e RAG



### Inspiração- **❓ Ajuda**: Exibe instruções de uso no terminal- **ChromaDB**: Banco de dados vetorial



✨ **DOS/Unix Terminals** (1980-1995)  - **🗑️ Limpar**: Limpa o terminal de chat- **Ollama**: Servidor de LLM local

✨ **BBS Systems** com ASCII art  

✨ **Monitores CRT** fosforescentes  - **PyMuPDF**: Processamento de PDFs

✨ **Cyberpunk Retro** aesthetic

### 4. Workflow de Uso

📄 **Documentação Completa**: Ver `VISUAL_RETRO_90s.md`

## 📝 Dependências

---

1. **Adicione documentos PDF**:

## ⚙️ Tecnologias e Configuração

   - Clique em "Adicionar PDF"Instale as dependências necessárias:

### Stack Tecnológico

   - Selecione um arquivo PDF do seu computador

| Componente | Tecnologia | Versão/Modelo |

|------------|------------|---------------|   - Aguarde a confirmação: "Arquivo adicionado com sucesso!"```bash

| **LLM** | Ollama | deepseek-r1:8b |

| **Embeddings** | Ollama | nomic-embed-text |pip install langchain langchain-community langchain-core langchain-chroma chromadb pymupdf

| **Re-Ranking** | Sentence-Transformers | ms-marco-MiniLM-L-6-v2 |

| **Vector DB** | ChromaDB | 1.3.4 |2. **Faça perguntas**:```

| **Framework** | LangChain | Community + Core |

| **GUI** | Tkinter | Python Standard Lib |   - Digite sua pergunta no campo de entrada na parte inferior

| **PDF Parser** | PyMuPDF | Latest |

   - Pressione Enter ou clique em "Enviar"## 🚀 Inicialização Rápida

### Arquitetura RAG com Re-Ranking

   - O bot processará e responderá baseado nos documentos

```

[Pergunta do Usuário]1. **Clone ou baixe o projeto**

        ↓

[Embedding com nomic-embed-text]3. **Liste os arquivos** (opcional):2. **Instale as dependências**

        ↓

[Busca Vetorial no ChromaDB] → Retorna 10 documentos   - Clique em "Listar Arquivos" para ver todos os PDFs adicionados3. **Certifique-se que o Ollama está rodando com o modelo deepseek-r1:8b**

        ↓

[Cross-Encoder Re-Ranking] → Score cada doc com ms-marco4. **Execute**: `python main.py`

        ↓

[Top 4 Documentos Selecionados]## ⚙️ Configuração5. **Adicione seus PDFs e comece a conversar!**

        ↓

[Contexto + Pergunta → deepseek-r1:8b]

        ↓

[Streaming de Resposta] → Output palavra-por-palavra### Modelos Configurados---

        ↓

[Citação de Fontes com Snippets]Os modelos podem ser alterados no arquivo `main.py`:

```

> **Nota**: Este sistema requer que o Ollama esteja rodando localmente com os modelos `deepseek-r1:8b` e `nomic-embed-text` instalados.

### Configurações Padrão```python

DB_PATH = './meu_armazem_chroma'  # Diretório do banco vetorial

```pythonEMBED_MODEL = 'nomic-embed-text'   # Modelo de embeddings

# main.pyLLM_MODEL = 'deepseek-r1:8b'       # Modelo de linguagem

DB_PATH = './meu_armazem_chroma'           # Banco vetorial local```

EMBED_MODEL = 'nomic-embed-text'            # Modelo embeddings

LLM_MODEL = 'deepseek-r1:8b'                # Modelo linguagem### Modelos Alternativos no Ollama

RERANKER_MODEL = 'ms-marco-MiniLM-L-6-v2'  # Cross-encoderVocê pode usar outros modelos disponíveis no Ollama:

INITIAL_K = 10                              # Docs iniciais

FINAL_K = 4                                 # Docs após re-rank**Para o LLM (geração de respostas):**

SNIPPET_LENGTH = 200                        # Chars por fonte- `llama3`

```- `mistral`

- `gemma`

### Modelos Alternativos- `phi3`



Você pode usar outros modelos do Ollama:Para trocar, baixe o modelo e altere `LLM_MODEL` no código:

```bash

**LLMs Compatíveis:**ollama pull llama3

- `llama3` - Meta's Llama 3```

- `mistral` - Mistral AI

- `gemma` - Google Gemma## 🗂️ Estrutura do Projeto

- `phi3` - Microsoft Phi-3

```

**Para trocar:**local_chatbot_RAG/

```bash├── main.py                    # Código principal da aplicação

ollama pull llama3├── README.md                  # Este arquivo

# Altere LLM_MODEL no main.py├── .gitignore                 # Arquivos ignorados pelo Git

```├── .venv/                     # Ambiente virtual (após criação)

└── meu_armazem_chroma/        # Banco de dados vetorial (criado automaticamente)

---```



## 🗂️ Estrutura do Projeto## 🔧 Troubleshooting



```### Erro: "No module named 'langchain_ollama'"

local_chatbot_RAG/**Solução**: Instale o pacote:

├── main.py                       # Aplicação principal (690+ linhas)```bash

├── README.md                     # Este arquivopip install langchain-ollama

├── VISUAL_RETRO_90s.md          # Doc visual retro completo```

├── RERANKING.md                 # Doc técnico re-ranking

├── STREAMING.md                 # Doc implementação streaming### Erro: "model 'nomic-embed-text' not found"

├── FONTES_MELHORADAS.md         # Doc sistema citações**Solução**: Baixe o modelo de embeddings:

├── .gitignore                   # Git ignore patterns```bash

├── .venv/                       # Ambiente virtual Pythonollama pull nomic-embed-text

└── meu_armazem_chroma/          # ChromaDB (criado auto)```

    ├── chroma.sqlite3

    └── [embeddings vectors]### Erro: "model 'deepseek-r1:8b' not found"

```**Solução**: Baixe o modelo de linguagem:

```bash

---ollama pull deepseek-r1:8b

```

## 🔧 Troubleshooting

### Erro: "Connection refused" ao adicionar PDF

### ❌ Erro: "No module named 'sentence_transformers'"**Solução**: Certifique-se que o Ollama está rodando:

```bash```bash

pip install sentence-transformersollama serve

``````



### ❌ Erro: "model 'nomic-embed-text' not found"### Programa não abre a janela

```bash**Solução**: Verifique se o tkinter está instalado:

ollama pull nomic-embed-text```bash

```python -m tkinter

```

### ❌ Erro: "model 'deepseek-r1:8b' not found"Se não funcionar, reinstale o Python com suporte a tkinter.

```bash

ollama pull deepseek-r1:8b## 📊 Requisitos de Sistema

```

- **RAM**: Mínimo 8GB (recomendado 16GB para modelos maiores)

### ❌ Erro: "Connection refused" ao adicionar PDF- **Armazenamento**: ~5GB para os modelos

**Causa**: Ollama não está rodando- **Sistema Operacional**: Windows 10/11, Linux, macOS

- **Conexão**: Necessária apenas para download inicial dos modelos

**Solução**:

```bash## 🛡️ Privacidade

ollama serve

```- ✅ Todos os dados são processados **localmente**

- ✅ Nenhuma informação é enviada para servidores externos

### ❌ Programa não abre a janela- ✅ Seus documentos ficam apenas no seu computador

**Causa**: Tkinter não instalado

## 🎨 Interface

**Solução**:

```bash### Design:

# Teste tkinter- **Tema**: Modo escuro moderno

python -m tkinter- **Terminal integrado**: Para interação e visualização de respostas

- **Botões intuitivos**: Fácil navegação

# Se falhar, reinstale Python com suporte GUI

```### Layout:

```

### ❌ Re-ranking lento na primeira vez┌─────────────────────────────────────────────────┐

**Causa**: Download do modelo ms-marco (~90MB)│          🤖 Chatbot RAG                         │

├─────────────────────────────────────────────────┤

**Solução**: Aguarde o download automático na primeira execução.│ [📄 PDF] [📁 Listar] [❓ Ajuda] [🗑️ Limpar]    │

├─────────────────────────────────────────────────┤

### ❌ Cores não aparecem corretamente│                                                 │

**Causa**: Tags de cor aplicadas incorretamente│               💻 Terminal Chat                  │

│  ┌─────────────────────────────────────────┐    │

**Solução**: As cores foram corrigidas! Se persistir, reinicie o programa.│  │ Bot: Bem-vindo ao Chatbot RAG!          │    │

│  │                                         │    │

---│  │                                         │    │

│  └─────────────────────────────────────────┘    │

## 📊 Requisitos de Sistema│                                                 │

│ [_______________entrada_______________] [Enviar]│

| Requisito | Mínimo | Recomendado |└─────────────────────────────────────────────────┘

|-----------|--------|-------------|```

| **RAM** | 8GB | 16GB |

| **Armazenamento** | 5GB | 10GB |## 🛠️ Tecnologias Utilizadas

| **CPU** | 4 cores | 8+ cores |

| **GPU** | Não necessária | Acelera LLM |- **Python 3.8+**

| **SO** | Windows 10 | Windows 11 |- **Tkinter**: Interface gráfica

| **Python** | 3.8 | 3.10+ |- **LangChain**: Framework para IA e RAG

- **ChromaDB**: Banco de dados vetorial

**Nota**: Modelos LLM maiores (70B+) requerem 32GB+ RAM.- **Ollama**: Servidor de LLM local

- **PyMuPDF**: Processamento de PDFs

---

## 📝 Licença

## 🛡️ Privacidade e Segurança

Este projeto está sob a licença MIT.

✅ **100% Local**: Nenhum dado enviado para nuvem  

✅ **Offline**: Funciona sem internet após setup  ## 🤝 Contribuições

✅ **Privacidade Total**: Seus PDFs ficam no seu PC  

✅ **Sem Telemetria**: Sem rastreamento ou analytics  Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

✅ **Open Source**: Código auditável  

## 📧 Contato

---

- GitHub: [@victormedrado99](https://github.com/victormedrado99)

## 📚 Documentação Adicional- Repositório: [local_chatbot_RAG](https://github.com/victormedrado99/local_chatbot_RAG)



- 📘 **VISUAL_RETRO_90s.md** - Guia completo do visual retro---

- 📗 **RERANKING.md** - Técnica de re-ranking explicada

- 📙 **STREAMING.md** - Como funciona streaming de respostas**Desenvolvido com ❤️ usando Python, LangChain e Ollama**

- 📕 **FONTES_MELHORADAS.md** - Sistema de citações inteligentes

---

## 🎮 Features Implementadas

### ✅ Core RAG
- [x] Embeddings com nomic-embed-text
- [x] Vector store com ChromaDB persistente
- [x] LLM local com deepseek-r1:8b
- [x] Processamento de PDFs com PyMuPDF

### ✅ Advanced Features
- [x] Cross-encoder re-ranking (ms-marco)
- [x] Streaming de respostas palavra-por-palavra
- [x] Citações com snippets de 200 chars
- [x] Truncamento inteligente em limites de palavra

### ✅ Interface
- [x] GUI Tkinter com tema retro
- [x] Terminal integrado com cores diferenciadas
- [x] ASCII art borders e separadores
- [x] Botões estilo DOS com símbolos
- [x] Mensagens terminal com prefixos >>>
- [x] Cursor largo tipo DOS
- [x] Threading para operações assíncronas

### ✅ UX Improvements
- [x] Cores diferenciadas (bot verde, user ciano, fontes amarelo)
- [x] Feedback visual de processamento
- [x] Mensagens de erro amigáveis
- [x] Confirmações de operações
- [x] Status de carregamento de modelos

---

## 🚀 Roadmap Futuro

### Possíveis Melhorias
- [ ] Efeito scanlines CRT
- [ ] Glow/bloom em texto verde
- [ ] Sons retro (beeps, clicks)
- [ ] Boot sequence animada
- [ ] Suporte para outros formatos (TXT, DOCX)
- [ ] Histórico de conversas
- [ ] Export de respostas
- [ ] Configurações via GUI
- [ ] Temas customizáveis

---

## 📝 Licença

Este projeto está sob a licença **MIT**.

---

## 🤝 Contribuições

Contribuições são bem-vindas! 

**Como contribuir:**
1. Fork o projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona feature X'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📧 Contato

- **GitHub**: [@victormedrado99](https://github.com/victormedrado99)
- **Repositório**: [local_chatbot_RAG](https://github.com/victormedrado99/local_chatbot_RAG)

---

## 🎉 Agradecimentos

- **LangChain** - Framework RAG incrível
- **Ollama** - Servidor LLM local simplificado
- **ChromaDB** - Vector store eficiente
- **Sentence-Transformers** - Modelos de re-ranking
- **Comunidade Open Source** - Por tornar tudo possível

---

**Desenvolvido com 💚 usando Python, LangChain e Ollama**

```
╔════════════════════════════════════════════════╗
║  CHATBOT RAG v1.0 - TERMINAL RETRO EDITION    ║
║  "Bringing back the 90s, one terminal at a    ║
║   time..." - Powered by AI 🕹️                 ║
╚════════════════════════════════════════════════╝
```
