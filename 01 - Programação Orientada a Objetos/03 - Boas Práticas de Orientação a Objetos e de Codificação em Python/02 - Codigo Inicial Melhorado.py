class AtendimentoAlunos:
    codigo: int = 0
    fila = []
    alunos_atendidos = []
    senha_atual: str = ""

    def gerar_senhaatual(self) -> None:
        self.senha_atual = f"A{self.codigo}"

    def atualiza_fila(self) -> None:
        self.codigo += 1
        self.gerar_senhaatual()
        self.fila.append(self.senha_atual)

    def atende_aluno(self, guiche: str) -> str:
        aluno_atual = self.fila.pop(0)
        self.alunos_atendidos.append(aluno_atual)
        return f"{aluno_atual} - Guichê {guiche}"


secretaria = AtendimentoAlunos()
secretaria.atualiza_fila()
secretaria.atualiza_fila()
secretaria.atualiza_fila()
secretaria.atualiza_fila()

print("\t=== Pessoas atualmente na fila:", secretaria.fila)

print(secretaria.atende_aluno("3"))
print(secretaria.atende_aluno("1"))

print("\t=== Pessoas atendidas:", secretaria.alunos_atendidos)

print("\t=== Pessoas atualmente na fila:", secretaria.fila)