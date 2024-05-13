# Listas

numeros = [1, 10, 100, 1000]
print(numeros)

# Imprimir o elemento de índice 2 - inicia no 0
print(numeros[2])

# Operações de Listas

# Incluir 2 itens na lista usando +=
numeros += [10000, 100000]
print(numeros)

# Incluir 1 item na lista usando o append
numeros.append(1000000)
print(numeros)

# Substituir os itens nas posições 1 e 2 por 7
# [índice_incluído:índice_excluído]
numeros[1:3] = [7]
print(numeros)

# Remover os itens nas posições 1 e na lista
numeros[1:3] = []
print(numeros)

# Tamanho da lista
print(len(numeros))
