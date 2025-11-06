"""
Script para criar o executável do Chatbot RAG
Execute: python build_exe.py
"""
import os
import sys
import subprocess

def build_executable():
    print("🔨 Criando executável do Chatbot RAG...")
    print("Isso pode levar alguns minutos...\n")
    
    # Comando PyInstaller
    command = [
        'pyinstaller',
        '--onefile',                    # Arquivo único
        '--windowed',                   # Sem console (apenas GUI)
        '--name=ChatbotRAG',            # Nome do executável
        '--icon=NONE',                  # Sem ícone customizado
        '--clean',                      # Limpar cache
        'main.py'
    ]
    
    try:
        # Executar PyInstaller
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        print("✅ Executável criado com sucesso!")
        print(f"\n📁 Localização: dist\\ChatbotRAG.exe")
        print("\n📝 Instruções:")
        print("1. Certifique-se que o Ollama está rodando")
        print("2. Execute ChatbotRAG.exe")
        print("3. Adicione PDFs e comece a usar!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar executável: {e}")
        print(f"Saída: {e.stdout}")
        print(f"Erro: {e.stderr}")
        sys.exit(1)

if __name__ == '__main__':
    build_executable()
