import streamlit as st
import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

# Configurações (com fallback)
LM_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1")
MODELO = os.getenv("MODELO_CODIGO", "hermes-3-llama-3.2-3b")
SCILAB_PATH = os.getenv("SCILAB_PATH", r"C:\\Program Files\\scilab-2026.0.1\\bin\\WScilex.exe")

st.set_page_config(page_title="Tradutor Scilab", layout="centered")
st.title("🧪 Tradutor de Scilab com IA Local")

# Sidebar com status
with st.sidebar:
    st.header("🔧 Status")
    st.write(f"**Modelo:** {MODELO}")
    st.write(f"**LM Studio:** {'✅' if requests.get(LM_URL).status_code == 200 else '❌'} (porta 1234)")
    st.write(f"**Scilab:** {'✅' if os.path.exists(SCILAB_PATH) else '❌'} no caminho informado")

# Entrada
descricao = st.text_area("📝 Descreva o que você quer no Scilab:", height=150)

if st.button("🚀 Gerar e Executar"):
    if not descricao.strip():
        st.warning("Digite uma descrição.")
    else:
        # 1. Gerar código
        with st.spinner("Gerando código com IA local..."):
            prompt = f"Gere apenas código Scilab (sem explicações) para: {descricao}"
            payload = {
                "model": MODELO,
                "messages": [
                    {"role": "system", "content": "Você é um especialista em Scilab. Responda apenas com código Scilab puro, sem markdown."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.2,
                "max_tokens": 1000
            }
            try:
                resp = requests.post(f"{LM_URL}/chat/completions", json=payload)
                codigo = resp.json()["choices"][0]["message"]["content"]
                codigo = codigo.replace("```scilab", "").replace("```", "").strip()
                st.code(codigo, language="scilab")
            except Exception as e:
                st.error(f"Erro na IA: {e}")
                st.stop()

        # 2. Executar Scilab
        with st.spinner("Executando no Scilab..."):
            os.makedirs("temp", exist_ok=True)
            arquivo = "temp/script.sce"
            with open(arquivo, "w", encoding="utf-8") as f:
                f.write(codigo)

            try:
                cmd = [SCILAB_PATH, "-nb", "-f", arquivo]
                resultado = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if resultado.stderr:
                    st.error(f"Erro no Scilab:\n```\n{resultado.stderr}\n```")
                else:
                    st.success("✅ Executado com sucesso! Verifique a janela do Scilab.")
            except FileNotFoundError:
                st.error(f"Executável não encontrado: {SCILAB_PATH}")
            except Exception as e:
                st.error(f"Erro na execução: {e}")
                