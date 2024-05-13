class Carro:

    def __init__(self):
        self.cor = "preto"

# um novo carro é criado com a cor = "preto"
carro_1 = Carro()
print(carro_1.cor)

carro_1.cor = "branco"
print(carro_1.cor)

print(" ")

class Carro2:

    def __init__(self, cor):
        self.cor = cor

# um novo carro é criado com cor = "azul"
carro_2 = Carro2("azul")
print(carro_2.cor)

carro_2.cor = "branco"
print(carro_2.cor)
