from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from typing import List

def create_vectorstore(chunks: List[str], persist_dir: str = "db") -> Chroma:
    """
    Cria uma base vetorial (VectorStore) persistente a partir de chunks de texto.

    Args:
        chunks (List[str]): Lista de textos divididos em trechos (chunks) para indexação.
        persist_dir (str): Diretório onde a base vetorial será armazenada.

    Returns:
        Chroma: Instância do Chroma com os documentos indexados.
    """
    # Inicializa os embeddings da OpenAI
    embeddings = OpenAIEmbeddings()

    # Transforma cada chunk de texto em um objeto Document
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Cria a base vetorial Chroma com os documentos
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    # Persiste os vetores em disco
    vectordb.persist()

    return vectordb