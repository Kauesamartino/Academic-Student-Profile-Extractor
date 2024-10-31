# Sistema de Consulta Acadêmica 🎓

## Sobre o Projeto
Este é um sistema de consulta acadêmica inteligente que utiliza LangChain e OpenAI para processar perguntas em linguagem natural sobre estudantes e instituições de ensino.

## Funcionalidades
O sistema é capaz de:
- Consultar dados de estudantes específicos
- Criar e comparar perfis acadêmicos
- Analisar compatibilidade entre estudantes para estudos em grupo
- Buscar informações sobre universidades
- Recomendar instituições com base no perfil do estudante
- Avaliar chances de admissão em diferentes universidades

## Tecnologias Utilizadas
- Python
- LangChain
- OpenAI
- Agents (LangChain)

## Como Usar
1. Instale as dependências necessárias:
```bash
pip install langchain openai
```
## Exemplos de Uso

### Faça consultas
```python
pergunta = "Quais os dados de Ana?"
response = agent_executor.invoke({"input": pergunta})
```


## Tipos de Consultas Suportadas
- Dados individuais de estudantes
- Comparações entre estudantes
- Informações sobre universidades
- Recomendações personalizadas
- Análise de compatibilidade para estudos em grupo
- Avaliação de chances de admissão

## Configuração
Para usar este projeto, você precisará:
1. Uma chave de API da OpenAI
2. As dependências Python instaladas
3. Configurar suas variáveis de ambiente:
```bash
export OPENAI_API_KEY="sua_chave_de_api"
```


## Contribuindo
Sinta-se à vontade para contribuir com este projeto através de pull requests ou reportando issues.

## Licença
[MIT License](LICENSE)
