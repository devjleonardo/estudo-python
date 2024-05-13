# Paradigmas de Programação

### Programação Procedural

A programação procedural, também conhecida como programação estruturada, é baseada no conceito de chamadas a 
procedimentos, que são rotinas, métodos e funções. Este paradigma é fundamental para a compreensão de como os dados e 
as operações sobre os dados são estruturados em programas simples e complexos.

### Programação Orientada a Objetos (POO)

A programação orientada a objetos (POO) é uma abordagem baseada na ideia de "objetos", que podem encapsular dados e 
métodos juntos como uma unidade. Este paradigma é uma aproximação da visão de mundo que temos, trabalhando com 
transformação, manipulação e utilização de objetos.

## Classes e Objetos

Em Programação Orientada a Objetos (POO), as classes são para objetos assim como formas são para bolos. Por exemplo, 
podemos usar uma única forma para preparar vários tipos de bolos, como bolo de chocolate, bolo de laranja, bolo de fubá, 
entre outros. A forma dá a estrutura básica ao bolo, enquanto os ingredientes específicos e as decorações fazem cada 
bolo único.

Da mesma maneira, em POO, uma classe define a estrutura e o comportamento dos objetos que são criados a partir dela. 
Cada objeto criado, conhecido como instância, pode ter características próprias, mas todos compartilham a mesma 
estrutura e comportamentos definidos pela classe.

### Exemplo

Imagine uma classe `Bolo` que define atributos como `sabor`, `peso` e métodos como `assar()` e `decorar()`. Podemos 
criar diferentes instâncias de `Bolo`:

```python
bolo_chocolate = Bolo(sabor="chocolate", peso="500g")
bolo_laranja = Bolo(sabor="laranja", peso="450g")

bolo_chocolate.assar()
bolo_laranja.decorar()
````

### Classe
Uma **classe** é uma estrutura que integra dados e comportamento. Representa, também, o conjunto de operações válidas 
que acessam e manipulam seus respectivos valores. A classe é usada para construir objetos. Ela é o projeto dos objetos, 
e fornece a descrição do comportamento (operações) comum e do estado (dados) destes.

### Objeto
Um **objeto** é uma instância de uma classe, e tem estado — seus dados, o que o objeto sabe sobre si mesmo — e 
comportamento, ou seja, o que o objeto faz. Os objetos construídos a partir de uma classe compartilham comportamento 
comum, sendo “instância” um sinônimo de “objeto”.

### Visualização Interativa

Para facilitar o entendimento, imagine as **classes** como moldes ou fôrmas de bolo, onde cada molde pode ser usado 
para criar diferentes bolos (objetos) com sabores distintos, mas todos mantendo a forma original. Cada bolo, então, 
terá suas características individuais (estado), como o sabor e a cobertura, além de métodos para serem preparados e 
servidos (comportamento).

## Exemplo Prático: Contato de Celular

### Compreendendo Classes e Objetos

É importante destacar que o comportamento de um objeto é definido por sua respectiva classe a partir de métodos, um 
conjunto de rotinas que operam sobre os dados. Já o estado de um objeto é definido por sua respectiva classe a partir de 
variáveis de instância, que representam os dados do objeto.

### Exemplo Diário

Vamos imaginar um exemplo mais próximo do dia a dia?

Imagine um objeto como um contato de seu celular. A entrada vazia pode ser considerada uma classe, e ela tem campos em 
branco, que chamamos de atributos.

Quando você preenche os dados de um contato, está criando uma instância (objeto). Os métodos da classe são as operações 
que você pode fazer sobre uma entrada específica, como: `consultar_telefone` e `editar_nome`.

```python
class Contato:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def editar_nome(self, novo_nome):
        self.nome = novo_nome

    def consultar_telefone(self):
        return self.telefone

# Criando um objeto Contato
contato_joao = Contato("João da Silva", "(00) 12345-7890", "joaodasilva@email.com.br", "Endereço de João")

# Usando métodos da classe
novo_telefone = contato_joao.consultar_telefone()
contato_joao.editar_nome("João S.")
```

## Pilares da Programação Orientada a Objetos (POO)

A Programação Orientada a Objetos é fundamentada em quatro conceitos principais que são conhecidos como os 
**pilares da POO**. Esses conceitos ajudam a projetar e organizar código de forma **eficiente**, **escalável** e 
**fácil de manter**.


### 1. Encapsulamento

**Definição:** Encapsulamento é o princípio pelo qual os **dados internos** de um objeto são protegidos de acesso 
externo. Isso é feito definindo métodos públicos para acessar e modificar os valores que são mantidos como privados 
dentro do objeto.


**Exemplo:** Considere uma classe `ContaBancaria` que protege o saldo do acesso direto e permite a manipulação do 
saldo apenas através de métodos como `depositar()` e `sacar()`.

```python
class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # Saldo é uma variável privada

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    def ver_saldo(self):
        return self.__saldo
```

### 2. Abstração

**Abstração** Abstração permite lidar com complexidades criando modelos simplificados que destacam apenas os aspectos 
**relevantes** de um contexto, enquanto escondem detalhes irrelevantes.

**Exemplo:** Uma interface `Veiculo` que define um método `mover()` pode ser implementada por várias classes como 
`Carro`, `Bicicleta` ou `Barco`, cada uma com uma implementação específica de como se move.

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo usando quatro rodas.")

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está se movendo usando duas rodas.")
```

### 3. Herança

**Herança** Herança é um mecanismo pelo qual uma classe pode herdar características (dados e métodos) de outra classe.

**Exemplo:** Uma classe `Animal` com método `comer()` pode ser herdada por subclasses como `Cachorro` e `Gato`, que 
também podem ter métodos adicionais como `latir()` ou `miar()`.

```python
class Animal:
    def comer(self):
        print("Este animal está comendo.")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo.")

class Gato(Animal):
    def miar(self):
        print("O gato está miando.")
```

### 4. Polimorfismo

**Polimorfismo** Polimorfismo é a capacidade de uma função de agir de maneira diferente com base no objeto que a invoca.

**Exemplo:** Usando a herança da classe `Animal`, podemos chamar o método `comer()` em qualquer instância de `Animal`, 
seja ela `Cachorro` ou `Gato`, e o método `emitir_som()` pode ter implementações distintas.

```python
class Animal:
    def comer(self):
        print("Este animal está comendo.")

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro late.")

class Gato(Animal):
    def emitir_som(self):
        print("O gato mia.")

animais = [Cachorro(), Gato()]
for animal in animais:
    animal.comer()  # Comportamento comum
    animal.emitir_som()  # Comportamento específico
```

## Métodos

Dentro das classes, é possível definir os métodos que representam as ações que os objetos criados a partir delas 
poderão realizar. Um método recebe pelo menos um parâmetro: a instância da classe, representada pela palavra reservada 
`self`. Esse parâmetro permite saber a que instância se referem os atributos.

Na declaração do método, é preciso declarar `self` explicitamente, mas, ao chamar o método em um objeto, `self` é 
passado automaticamente.

### Exemplo de Métodos em uma Classe

Definimos uma classe `Pessoa`, que tem dois métodos:

- `__init__`, que inicializa o atributo nome durante a criação da instância;
- `__str__`, que converte uma `Pessoa` para string.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome

pessoa_1 = Pessoa("João")
print(pessoa_1)  # Saída: João

pessoa_2 = Pessoa("Maria")
print(pessoa_2)  # Saída: Maria
```

## Atributos

Existem três tipos de variáveis que podem ser declaradas dentro de uma classe:

### Atributos de Classe
São atributos ligados à classe, e todas as instâncias da classe compartilham o mesmo atributo.

### Atributos de Instância
São específicos para cada instância, podendo ter valores diferentes de uma instância para outra.

### Variáveis de Método
Existem apenas enquanto a função está sendo executada.

### Exemplo de Classe com Diferentes Tipos de Atributos

A classe `ListaDeNumeros` exemplifica o uso de atributos de instância. Cada instância desta classe mantém sua própria 
lista de números, e os métodos `soma` e `media` operam sobre esses números.

```python
class ListaDeNumeros:
    def __init__(self, numeros):
        self.numeros = numeros  # Atributo de instância

    def __str__(self):
        return ", ".join([str(n) for n in self.numeros])

    def soma(self):
        return sum(self.numeros)

    def media(self):
        return self.soma() / len(self.numeros)

minha_lista = ListaDeNumeros([1, 3, 5, 7, 9])
print(f"A soma de {minha_lista} é {minha_lista.soma()}")  # A soma de 1, 3, 5, 7, 9 é 25
print(f"A média de {minha_lista} é {minha_lista.media()}")  # A média de 1, 3, 5, 7, 9 é 5.
```