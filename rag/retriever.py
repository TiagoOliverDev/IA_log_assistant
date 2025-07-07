from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import BaseRetriever

def get_retriever(persist_dir: str = "db") -> BaseRetriever:
    """
    Inicializa um retriever com base em embeddings OpenAI e base vetorial ChromaDB.

    Args:
        persist_dir (str): Caminho para o diretório onde os vetores estão persistidos.

    Returns:
        BaseRetriever: Objeto retriever pronto para realizar buscas por similaridade semântica.
    """
    # Cria os embeddings a partir da API da OpenAI
    embeddings = OpenAIEmbeddings()

    # Carrega o banco vetorial persistido no diretório especificado
    vectordb = Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

    # Retorna um retriever configurado para retornar os 5 documentos mais similares
    return vectordb.as_retriever(search_kwargs={"k": 5})