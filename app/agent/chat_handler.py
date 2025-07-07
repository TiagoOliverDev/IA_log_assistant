from .agent_factory import build_agent

agent = build_agent()

def ask_ai(question: str) -> str:
    """
    Envia uma pergunta para o agente de IA e retorna a resposta.

    Args:
        question (str): Pergunta feita pelo usuário.

    Returns:
        str: Resposta gerada pelo agente. Caso ocorra erro, retorna mensagem de erro.
    """
    try:
        prompt = f"Responda em português: {question}"
        return agent.run(prompt)
    except Exception as e:
        return f"❌ Erro ao processar a pergunta: {str(e)}"