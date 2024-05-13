print("***********************************")
print("       O aluno foi aprovado?       ")
print("***********************************")

print(" ")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3  # calcula a média

if media >= 7:
    print("O aluno foi APROVADO! Sua média foi %.2f" % media)
elif media < 3:
    print("O aluno foi REPROVADO! Sua média foi %.2f" % media)
else:
    print("O aluno ficou em PROVA FINAL! Sua média foi %.2f" % media)
