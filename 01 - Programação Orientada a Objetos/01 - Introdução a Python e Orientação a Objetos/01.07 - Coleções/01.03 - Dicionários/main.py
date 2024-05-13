# Dicionários

# Criar e imprimir um dicionário
notas = {"Ana": 8, "Maria": 5, "Thais": 10}
print(notas)

# Acessar o valor correspondente à chave "Thais"
print(notas["Thais"])

# Incluir novo item
notas["Zaira"] = 9
print(notas)

# Remover item
del notas["Thais"]
print(notas)

# Checar se notas contém o item "Maria"
print("Maria" in notas)