from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
cliente = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

resposta = cliente.chat.completions.create(
  messages=[
  {
    "role": "system",
    "content": """
    Classifique o produto abaixo em uma das categorias: Higiene Pessoal, Moda ou Casa e dê uma descrição da categoria.
    """
  },
  {
    "role": "user",
    "content": """
    Escova de bambu
    """
  }
  ],
  model='gpt-3.5-turbo'
)
print(resposta.choices[0].message.content)