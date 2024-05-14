class antendimentoalunos:
    codigo = 0
    fila = []
    alunosatendidos = []
    senhaatual = ""

    def gerarsenhaatual(self):
        self.senhaatual = f"A{self.codigo}"
    def atualizafila(self):
        self.codigo += 1
        self.gerarsenhaatual()
        self.fila.append(self.senhaatual)
    def atendealuno(self, guiche):
        alunoatual = self.fila.pop(0)
        self.alunosatendidos.append(alunoatual)
        return f"{alunoatual} - Guichê {guiche}"


secretaria = antendimentoalunos()
secretaria.atualizafila()
secretaria.atualizafila()
secretaria.atualizafila()
secretaria.atualizafila()

print("\t=== Pessoas atualmente na fila:", secretaria.fila)

print(secretaria.atendealuno("3"))
print(secretaria.atendealuno("1"))

print("\t=== Pessoas atendidas:", secretaria.alunosatendidos)

print("\t=== Pessoas atualmente na fila:", secretaria.fila)