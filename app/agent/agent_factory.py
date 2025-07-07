import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from rag.retriever import get_retriever
from config.config import OPENAI_API_KEY

def build_agent():
    """
    Cria e retorna uma instância de agente de Perguntas e Respostas com base em Recuperação de Conhecimento (RAG).
    
    - Usa um modelo de linguagem da OpenAI para responder.
    - Integra um retriever que realiza busca semântica em base vetorial.
    """
    # Recuperador de documentos vetorizados (FAISS, Chroma, etc.)
    retriever = get_retriever()

    # LLM da OpenAI configurada com temperatura 0 para respostas determinísticas
    llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

    # Cadeia de QA baseada em recuperação semântica + LLM
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return qa_chain