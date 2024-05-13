class Calculadora:

    valor_interno = 5

    def adiciona(self, numero):
        # não podemos chamar a variável "valor_interno" sem "self" porque "valor" é um atributo de Calculadora
        return self.valor_interno + numero

total = Calculadora();
print("resultado = %d" % total.adiciona(3)) # self pegará o valor 5 de valor_interno e o valor 3 irá para o número