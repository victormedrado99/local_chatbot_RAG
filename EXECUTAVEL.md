# 🚀 Como Usar o ChatbotRAG.exe

## 📁 Localização do Executável

O arquivo executável está em:
```
dist\ChatbotRAG.exe
```

## ⚠️ PRÉ-REQUISITO IMPORTANTE

**ANTES DE EXECUTAR**, certifique-se que o Ollama está instalado e rodando com os modelos necessários!

### 1. Instalar o Ollama
- Baixe: https://ollama.ai/download
- Instale para Windows

### 2. Baixar os Modelos
Abra o PowerShell ou CMD e execute:

```bash
ollama pull nomic-embed-text
ollama pull deepseek-r1:8b
```

### 3. Verificar se está funcionando
```bash
ollama list
```

Você deve ver os dois modelos listados.

## 🎯 Executar o Chatbot

### Opção 1: Duplo clique
1. Navegue até a pasta `dist`
2. Duplo clique em `ChatbotRAG.exe`
3. A janela do chatbot abrirá

### Opção 2: Linha de comando
```bash
cd dist
ChatbotRAG.exe
```

## 📦 Distribuir o Executável

Para usar em outro computador:

1. **Copie o arquivo `ChatbotRAG.exe`** para qualquer pasta
2. **Instale o Ollama** no computador de destino
3. **Baixe os modelos** (comandos acima)
4. **Execute** o ChatbotRAG.exe

**Nota**: O executável tem ~200MB porque inclui todas as bibliotecas Python necessárias.

## 🔧 Solução de Problemas

### Erro: "Failed to execute script"
- Verifique se o Ollama está rodando
- Execute: `ollama serve` em um terminal separado

### Erro ao adicionar PDF
- Certifique-se que os modelos foram baixados
- Verifique: `ollama list`

### Janela não abre
- Execute pelo terminal para ver mensagens de erro
- Verifique o antivírus (pode estar bloqueando)

## 📊 Requisitos do Sistema

- **Windows 10/11** (64-bit)
- **RAM**: Mínimo 8GB (recomendado 16GB)
- **Espaço**: ~5GB para modelos + 200MB para executável
- **Ollama**: Deve estar instalado e rodando

## 🎨 Como Usar o Chatbot

1. **Adicionar PDF**: Clique no botão e selecione um PDF
2. **Listar Arquivos**: Ver todos os PDFs adicionados
3. **Fazer Pergunta**: Digite no campo inferior e pressione Enter
4. **Ajuda**: Clique para ver instruções
5. **Limpar**: Limpa o terminal

## 🛡️ Privacidade

✅ Tudo funciona localmente no seu computador
✅ Nenhum dado é enviado para internet
✅ Seus documentos ficam seguros na sua máquina

---

**Desenvolvido com ❤️ usando Python e Ollama**
