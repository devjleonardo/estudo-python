# Formatação

nome = "Belinha"
numero_inteiro = 7
numero_decimal = 7.584

print("Olá, meu nome é %s! tenho %d anos e %d reais"
      % (nome, numero_inteiro, numero_decimal)) # float impresso como int

print("Olá, meu nome é %s! tenho %d anos e %f reais"
      % (nome, numero_inteiro, numero_decimal)) # float impresso como float

print("Olá, meu nome é %s! tenho %d anos e %.2f reais"
      % (nome, numero_inteiro, numero_decimal)) # float impresso como float com 2 casas decimais