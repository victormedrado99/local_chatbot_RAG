# Novas Funcionalidades Implementadas

## 1. Citação de Fontes 📚

Agora, após cada resposta do bot, são exibidas as fontes consultadas com:
- Nome do arquivo de origem
- Número da página (quando aplicável)
- Trecho do documento usado (primeiras 150 caracteres)

### Exemplo de saída:
```
🤖 Resposta:
Python é uma linguagem de programação...

📚 Fontes consultadas:
1. teste_exemplo.txt
   "Python é uma linguagem de programação de alto nível, interpretada..."

2. documento.pdf (página 5)
   "A linguagem possui uma biblioteca padrão abrangente..."
```

## 2. Diferenciação de Cores 🎨

As mensagens agora têm cores diferentes para melhor visualização:

- **Verde (#00ff00)**: Mensagens do bot/sistema
- **Azul (#00bfff)**: Mensagens do usuário
- **Laranja (#ffa500)**: Fontes citadas
- **Branco (#ffffff)**: Prompt de comando

## 3. Melhorias Técnicas

### Tags de Cores
- Configuradas no `ScrolledText` usando `tag_configure`
- Aplicadas dinamicamente ao inserir texto
- Suporte para tags customizadas via parâmetro `color_tag`

### Método `_chat_worker` Atualizado
- Agora captura documentos relevantes diretamente do retriever
- Extrai metadados (source, page) de cada documento
- Formata e exibe fontes após a resposta
- Usa tuplas especiais para controlar cores via queue

### Sistema de Queue Aprimorado
- Suporte para mensagens com tags especiais (`__SOURCE_HEADER__`, `__SOURCE_ITEM__`)
- Processamento condicional baseado no tipo de mensagem
- Mantém compatibilidade com mensagens simples

## Como Testar

1. Execute o programa:
```powershell
.venv\Scripts\python.exe main.py
```

2. Adicione um documento (PDF ou TXT) usando o botão "Adicionar Documento"

3. Faça uma pergunta no terminal (após o prompt `>`)

4. Observe:
   - Sua pergunta em **azul**
   - A resposta do bot em **verde**
   - As fontes citadas em **laranja**

## Arquivos Modificados

- `main.py`: 
  - Método `create_widgets`: Adicionadas tags de cores
  - Método `write_to_terminal`: Suporte a cores customizadas
  - Método `show_prompt`: Usa cor branca
  - Método `_chat_worker`: Captura e exibe fontes
  - Método `check_queue`: Processa mensagens com tags

## Benefícios

✅ Melhor legibilidade com diferenciação visual
✅ Maior confiança nas respostas (fontes verificáveis)
✅ Transparência sobre quais documentos foram consultados
✅ Interface mais profissional e intuitiva
