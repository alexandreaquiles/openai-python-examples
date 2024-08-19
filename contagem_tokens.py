import tiktoken

modelo_mini = "gpt-4o-mini"
codificador = tiktoken.encoding_for_model(modelo_mini)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo_mini} é de ${(len(lista_tokens)/1_000_000) * 0.15}")

modelo = "gpt-4o"
codificador = tiktoken.encoding_for_model(modelo)
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
print(f"Custo para o modelo {modelo} é de ${(len(lista_tokens)/1_000_000) * 5}")

print(f"O custo do {modelo} é de {5/0.15} maior que o do {modelo_mini}")
