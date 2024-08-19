from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
modelo='gpt-4'
prompt_sistema = """
Você é um categorizador de produtos.
Você deve assumir as categorias presentes na lista abaixo.

# Lista de Categorias Válidas

  - Moda Sustentável
  - Produtos para o Lar
  - Beleza Natural
  - Eletrônicos Verdes
  - Higiene Pessoal

# Formato da Saída
  Produto: Nome do Produto
  Categoria: apresente a categoria do produto

# Exemplo de Saída
  Produto: Escova elétrica com recarga solar
  Categoria: Eletrônicos Verdes
"""

prompt_usuario = input('Digite o nome de um produto sustentável: ')

resposta = cliente.chat.completions.create(
  messages=[
  {
    "role": "system",
    "content": prompt_sistema
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