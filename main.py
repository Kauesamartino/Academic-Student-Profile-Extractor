from langchain.agents import AgentExecutor
from agent import AgentOpenAIFunctions

''' Exemplos de perguntas:
pergunta = "Quais os dados de Ana?"
pergunta = "Quais os dados de Bianca?"
pergunta = "Quais os dados de Ana e da Bianca?"
pergunta = "Crie um perfil acadêmico para a Ana!"
pergunta = "Compare o perfil acadêmico da Ana com o da Bianca!"
pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com a Bianca?"
pergunta = "Tenho sentido Ana desanimada com cursos de matemática. Seria uma boa parear ela com o Marcos?"
pergunta = "Quais os dados da USP?"
pergunta = "Quais os dados da uNiCAmP?"
pergunta = "Quais os dados da uNi CAmP?"
pergunta = "Quais os dados da uNicomP?"
pergunta = "Dentre USP e UFRJ, qual você recomenda para a acadêmica Ana?"
pergunta = "Quais as faculdades com melhores chances para Ana entrar?"
pergunta = "Alem das faculdades favoritas da Ana, existem outras faculdades. Considere elas também. Quais Ana possui mais chance de entrar?"
'''
pergunta = input("Digite sua pergunta: ")

agent = AgentOpenAIFunctions()
agent_executor = AgentExecutor(agent=agent.agent, 
                            tools=agent.tools, 
                            verbose=True)

response = agent_executor.invoke({"input": pergunta})
print(response)