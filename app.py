from requests import post
import streamlit as st

# SECTION - 1. Título do aplicativo
st.title("Contador de Palavras com FastAPI")

# SECTION - 2. Área para fazer o upload do arquivo
uploaded_file = st.file_uploader("Faça upload de um arquivo .txt", type="txt")

if uploaded_file is not None:
    # SECTION - 3. Enviar o arquivo para a API
    url_de_requisicao = "http://127.0.0.1:8000/upload/"

    files = {"file": uploaded_file}
    resposta = post(url_de_requisicao, files=files)

    # SECTION - 4. Analisando a resposta
    if resposta.status_code == 200:
        data = resposta.json()
        st.write("Nome do arquivo:", data["filename"])
        st.write("Total de palavras:", data["total_de_palavras"])

    else:
        st.error(f"Erro ao enviar o arquivo: {resposta.status_code} - {resposta.text}")
