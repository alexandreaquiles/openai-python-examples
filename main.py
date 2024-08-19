from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
modelo='gpt-3.5-turbo'
prompt_sistema = """
Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa e dê uma descrição da categoria.
"""

prompt_usuario = """
Escova de bambu
"""

resposta = cliente.chat.completions.create(
  messages=[
  {
    "role": "system",
    "content":prompt_sistema
  },
  {
    "role": "user",
    "content": prompt_usuario
  }
  ],
  model=modelo,
  temperature=0,
  max_tokens=200
)

print(f"\n{resposta.choices[0].message.content}")