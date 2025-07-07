# 📊 Log Assistant com IA (LangChain + OpenAI + RAG)

Este projeto é um **assistente inteligente de análise de logs**, construído com **LangChain**, **OpenAI** e **Streamlit**, utilizando **RAG** (Retrieval-Augmented Generation) para fornecer **respostas contextuais** com base nos seus arquivos `.log`.

---

## 🚀 Funcionalidades

- 🔍 **Upload e análise de arquivos `.log` ou `.txt`**
- 🧠 **Integração com LLM + RAG** para contextualização precisa
- 💬 **Campo de input para perguntas em linguagem natural**
- 📄 **Geração de PDF com resumos de erros e avisos**
- 🇧🇷 Respostas 100% em **português**
- 🐳 Totalmente containerizado com **Docker + Docker Compose**

---

## 🗂️ Estrutura do Projeto

```bash
log_assistant/
├── app/
│   ├── main.py               # Interface Streamlit
│   └── agent/
│       ├── chat_handler.py   # Função ask_ai()
│       ├── agent_factory.py  # Criação do agente
│       └── tools.py          # Ferramentas auxiliares
├── rag/
│   ├── loader.py             # Carrega e divide os logs em chunks
│   ├── retriever.py          # Configura o mecanismo de busca
│   └── vectorstore.py        # Cria a base vetorial com Chroma
├── data/
│   └── sample.log            # Arquivos de exemplo
├── config/
│   └── config.py             # OPENAI_API_KEY e configurações
├── .env                      # Variáveis de ambiente
├── requirements.txt          # Dependências do projeto
├── Dockerfile                # Build da imagem Docker
├── docker-compose.yml        # Orquestração com Docker Compose
└── README.md                 # Este arquivo
```


## ⚙️ Como Executar o Projeto

### 🔧 Pré-requisitos
- Docker  
- Docker Compose  
- Chave da OpenAI válida  

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/log_assistant.git
cd log_assistant


OPENAI_API_KEY=sk-sua-chave-aqui

3. Execute com Docker Compose

docker-compose up --build

Depois, acesse: http://localhost:8501

```


### 💡 Exemplos de Perguntas
```bash
Quantos erros aconteceram nos logs?

Qual foi o último erro registrado?

Qual foi o maior tempo de resposta?

Me diga o horário com mais requisições.

Houve falhas de conexão com o banco?

Qual IP mais aparece nos logs?
```


### 🧩 Tecnologias Utilizadas
```bash
LangChain

OpenAI API

Streamlit

ChromaDB

Python 3.11

Docker
```


### ⚠️ Aviso de Segurança
Este projeto executa leitura de arquivos .log e alimenta uma IA. Garanta que os logs não contenham dados sensíveis. Para ambientes críticos, implemente filtros e sanitização de dados.


## 📚 Licença

Este projeto é open-source e está sob a licença [MIT](LICENSE).

---

## 👨‍💻 Desenvolvido por

**Tiago Oliveira**  
Analista desenvolvedor e Engenheiro de dados em formação

- 💼 [LinkedIn](https://www.linkedin.com/in/tiago-oliveira-49a2a6205/)
- 💻 [GitHub](https://github.com/TiagoOliverDev)