# Definição da classe
class Aluno:

    def __init__(self):
        self.nome = "Zé"
        self.idade = 18

    def dobra_idade(self):
        return self.idade * 2

# Instanciação dos objetos

aluno_1 = Aluno()
aluno_1.nome = "Maria" # definindo o nome do aluno_1 é "Maria"

aluno_2 = Aluno()
aluno_2.idade = 21 # definindo que a idade do aluno_2 é 21

print(aluno_1.nome) # imprime Maria (valor que definimos)
print(aluno_2.nome) # imprime Zé (valor default)

print(aluno_1.dobra_idade()) # dobra a idade 18 (valor default)
print(aluno_2.dobra_idade()) # dobra a idade 21 (valor que definimos)

# ao mudar o valor de nome em aluno_1, o aluno_2 continua inalterado
aluno_1.nome = "Ana"
print("Nome do aluno_1:", aluno_1.nome)
print("Nome do aluno_2:", aluno_2.nome)