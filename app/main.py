import streamlit as st
from agent.chat_handler import ask_ai
from rag.loader import load_log_file, split_log_text
from rag.vectorstore import create_vectorstore
from app.utils.pdf_generator import generate_pdf
import os

st.set_page_config(page_title="Log Assistant", layout="wide")
st.title("🧠 Assistente de Logs com IA")

def extrair_erros_avisos(texto):
    erros = []
    avisos = []
    for linha in texto.splitlines():
        linha_lower = linha.lower()
        if "erro" in linha_lower or "fail" in linha_lower or "exception" in linha_lower:
            erros.append(linha.strip())
        elif "aviso" in linha_lower or "warning" in linha_lower:
            avisos.append(linha.strip())
    return erros, avisos

def filtrar_logs_por_nivel(texto, nivel):
    nivel = nivel.lower()
    linhas_filtradas = []
    for linha in texto.splitlines():
        linha_lower = linha.lower()
        if nivel == "todos":
            linhas_filtradas.append(linha)
        elif nivel == "erro" and ("erro" in linha_lower or "fail" in linha_lower or "exception" in linha_lower):
            linhas_filtradas.append(linha)
        elif nivel == "aviso" and ("aviso" in linha_lower or "warning" in linha_lower):
            linhas_filtradas.append(linha)
        elif nivel == "info" and not ("erro" in linha_lower or "fail" in linha_lower or "exception" in linha_lower or "aviso" in linha_lower or "warning" in linha_lower):
            linhas_filtradas.append(linha)
    return linhas_filtradas

uploaded_file = st.file_uploader("Envie seu arquivo de log", type=["log", "txt"])

if uploaded_file:
    file_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    st.success("Arquivo recebido!")

    texto_log = load_log_file(file_path)
    chunks = split_log_text(texto_log)
    create_vectorstore(chunks)

    st.info("✅ Base vetorial criada com sucesso!")

    erros, avisos = extrair_erros_avisos(texto_log)

    if erros or avisos:
        pdf_buffer = generate_pdf(erros, avisos)
        st.download_button(
            label="📄 Baixar relatório PDF de erros e avisos",
            data=pdf_buffer,
            file_name="relatorio_logs.pdf",
            mime="application/pdf"
        )
    else:
        st.info("Nenhum erro ou aviso encontrado para gerar relatório.")

    # **Filtro para mostrar logs**
    st.markdown("---")
    st.header("📋 Visualização dos Logs")
    nivel_selecionado = st.selectbox("Selecione o nível de log para exibir:", ["Todos", "Info", "Aviso", "Erro"])

    logs_filtrados = filtrar_logs_por_nivel(texto_log, nivel_selecionado)
    st.text_area(f"Logs filtrados - Nível: {nivel_selecionado}", value="\n".join(logs_filtrados), height=300)

    user_question = st.text_input("❓Faça uma pergunta sobre os logs:")
    if user_question:
        with st.spinner("Consultando IA..."):
            answer = ask_ai(user_question)
            st.success(answer)
