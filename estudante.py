import os
import json
from typing import List
import pandas as pd
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

def buscar_dados_de_estudante(estudante):
        dados = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/3860-langchain-agentes-python/projeto-base/documentos/estudantes.csv')
        dados_do_estudante = dados[dados['USUARIO'] == estudante]
        if dados_do_estudante.empty:
            return {}
        return dados_do_estudante.iloc[:1].to_dict()
    
class ExtratorDeEstudante(BaseModel):
    estudante: str = Field("O nome do estudante informado, sempre em letras minúsculas.")

class DadosDeEstudante(BaseTool):
    name = "DadosDeEstudante"
    description = """Esta ferramenta extrai o histórico de preferências de um estudante de acordo com seu histórico.
    Passe para essa ferramenta como argumento o nome do estudante."""

    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o-mini",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=ExtratorDeEstudante)
        template = PromptTemplate(template="""Você deve analisar a entrada a seguir e extrair o nome informado em letras minúsculas.                               
Entrada: 
--------------------
{input}
--------------------                          
                                Formato de saida:
                                {format_instructions}""",
                                input_variables=["dados_do_estudante"],
                                partial_variables={"format_instructions": parser.get_format_instructions()})
        chain = template | llm | parser
        response = chain.invoke({"input": input})
        estudante = response['estudante']
        estudante = estudante.lower().strip()
        dados = buscar_dados_de_estudante(estudante)
        return json.dumps(dados)
    
class Nota(BaseModel):
    area:str = Field("nome da area de conhecimento")
    nota:float = Field("nota na area de conhecimento")

class PerfilAcademicoDeEstudante(BaseModel):
    nome:str = Field("nome do estudante")
    ano_de_conclusao:int = Field("ano de conclusão")
    notas:List[Nota] = Field("nistas de notas ads disciplinas e áreas de conhecimento;")
    resumo:str = Field("resumo das principais características desse estudante de formaa a torna-lo unico e um otimo potencial de estudante para faculdades. Exemplo: só este estudante tem bla bla bla")

class PerfilAcademico(BaseTool):
     name = "PerfilAcademico"
     description = """Cria um perfil acadêmico para o estudante.
     Esta ferramenta requer como entrada todos os dados do estudante.
     Eu sou incapaz de buscar os dados dos estudantes.
     Você deve buscar os dados dos estudantes antes de me invocar."""

     def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o-mini",
                         api_key=os.getenv("OPENAI_API_KEY"))
        parser = JsonOutputParser(pydantic_object=PerfilAcademicoDeEstudante)
        template = PromptTemplate(template="""Formate o estudante para seu perfil academico
                                - Com os dados, identifique as opções de univeridade sugeridas e cursos compatíveis com o intersse do aluno.
                                - Destaque o perfil do aluno dando enfase principalmente naquilo que faz sentido para as instituições de interesse do aluno.
                                
                                Persona: você é uma consultora de carreira e precisa indicar com detalhes, riqueza, mas direta ao ponto para o estudante e faculdade as opções e consequências possíveis.
                                Informações atuais:
                                
                                {dados_do_estudante}
                                {format_instructions}
                                """,
                                input_variables=["dados_do_estudante"],
                                partial_variables={"format_instructions": parser.get_format_instructions()})
        chain = template | llm | parser
        response = chain.invoke({"dados_do_estudante": input})
        return response