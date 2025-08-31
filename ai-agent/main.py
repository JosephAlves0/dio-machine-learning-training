from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_ollama import OllamaLLM


ollama_host = "http://10.0.0.195:11434"
llm = OllamaLLM(model="llama3", base_url=ollama_host)

python_repl = PythonREPLTool()
tools = [python_repl]

prompt = PromptTemplate.from_template("""
Responda à seguinte pergunta o melhor que puder. Você tem acesso às seguintes ferramentas:

{tools}

Use o seguinte formato:

Pergunta: a pergunta que você deve responder
Pensamento: você deve sempre pensar no que fazer
Ação: a ação a ser executada, deve ser uma das ({tool_names})
Entrada da Ação: a entrada para a ação (apenas a string)
Observação: o resultado da Ação
... (este Pensamento/Ação/Entrada da Ação/Observação pode se repetir várias vezes)
Pensamento: cheguei a uma resposta final
Resposta Final: a resposta final à pergunta original

Comece!

Pergunta: {input}
{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executor.invoke({"input": "Qual é a soma de 123 e 456?"})
print(response['output'])