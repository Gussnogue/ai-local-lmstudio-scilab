# 🧪 Tradutor de Scilab com IA Local

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)
![LM Studio](https://img.shields.io/badge/LM%20Studio-Local%20AI-green)
![Scilab](https://img.shields.io/badge/Scilab-2026%2B-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Um aplicativo que traduz descrições em linguagem natural para código **Scilab** usando modelos de IA locais (via **LM Studio**). Basta digitar o que você quer calcular ou plotar, e a IA gera o script e o executa automaticamente: tudo 100% offline, sem depender de APIs externas.

![Demonstração](images/demo.gif) *Exemplo: "plote a função seno de 0 a 2pi"*

---

## ✨ Funcionalidades

- ✅ **Interpretação em Português:** Descreva o problema em linguagem natural.
- ✅ **Geração Automática de Código:** IA local (ex: Hermes 3 Llama 3.2 3B) produz o script Scilab.
- ✅ **Execução Integrada:** O código é executado no Scilab automaticamente.
- ✅ **Privacidade Total:** Tudo roda na sua máquina — sem envio de dados para a nuvem.
- ✅ **Interface Simples:** Feita com Streamlit, fácil de usar e modificar.

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.10+**
- **LM Studio** (com modelo de instrução, ex: `hermes-3-llama-3.2-3b`)
- **Scilab 2026+** (ou versão compatível)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Gussnogue/ai-local-lmstudio-scilab.git
   cd ai-local-lmstudio-scilab
   ```
2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   # Windows (CMD)
   venv\Scripts\activate.bat
   # Linux/Mac
   source venv/bin/activate
   
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   
4. **Configure as variáveis de ambiente. Crie um arquivo .env na raiz com o seguinte conteúdo:**
   ```bash
   LM_STUDIO_URL=http://localhost:1234/v1
   MODELO_CODIGO=hermes-3-llama-3.2-3b
   SCILAB_PATH=C:/Program Files/scilab-2026.0.1/bin/WScilex-cli.exe
Ajuste o caminho do Scilab para a sua instalação. Use barras normais (/).

5. **Inicie o LM Studio**
   ```
   Abra o LM Studio
   Carregue o modelo escolhido
   Ative o servidor local na porta 1234
7. **Execute o aplicativo**
   ```bash
   streamlit run app.py

## 📄 Licença
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📬 Contato
[Gustavo Nogueira](https://www.linkedin.com/in/gustavo-nogueira-6077401b9/)
LinkedIn
