from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

# SECTION - 1. Criando a instância do FastApi
app = FastAPI(
    title="API de Contagem de Palavras",
    description="Uma API básica desenvolvida para fins de aprendizado. Contagem de palavras em um .txt",
    version="0.1",
)


# SECTION - 2. Definindo o Endpoint POST /upload/
@app.post("/upload/")
async def contar_palavras_no_arquivo(
    file: UploadFile = File(...),
) -> dict[str, str | int]:
    """
    Recebe um arquivo .txt, conta o número de palavras e retorna o nome do arquivo e contagem."""

    # SECTION - 3. Leitura do conteúdo do arquivo
    conteudo = await file.read()

    # SECTION - 4. Decodificando o contéudo para texto(utf-8 nesse caso)
    try:
        conteudo_em_texto = conteudo.decode("utf-8")

    except UnicodeDecodeError:
        try:
            conteudo_em_texto = conteudo.decode("latin-1")

        except UnicodeDecodeError:
            return JSONResponse(
                {
                    "error": "Não foi possível decodificar o arquivo. Use UTF-8 ou Latin-1."
                },
                status_code=400,
            )

    # SECTION - 5. Contagem de palavras
    palavras = conteudo_em_texto.split()
    total_de_palavras = len(palavras)

    return {"filename": file.filename, "total_de_palavras": total_de_palavras}
