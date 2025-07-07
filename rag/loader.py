from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_log_file(file_path: str) -> str:
    """
    Carrega o conteúdo de um arquivo de log.

    Args:
        file_path (str): Caminho para o arquivo de log (.log ou .txt).

    Returns:
        str: Conteúdo do arquivo como texto bruto.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def split_log_text(text: str) -> list[str]:
    """
    Divide o texto dos logs em pedaços menores para facilitar o embedding e busca vetorial.

    Usa o `RecursiveCharacterTextSplitter` para preservar a estrutura sempre que possível.

    Args:
        text (str): Texto completo do log.

    Returns:
        list[str]: Lista de trechos de texto.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,     # Tamanho máximo de cada pedaço
        chunk_overlap=100    # Sobreposição para manter contexto entre chunks
    )
    return splitter.split_text(text)