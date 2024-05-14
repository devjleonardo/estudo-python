# Classe AtendimentoPessoas

import abc


class AtendimentoPessoas:
    codigo: int = 0
    fila = []
    pessoas_atendidas = []
    senha_atual: str = ""

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def atende_pessoa(self, guiche: int):
        ...

    @abc.abstractmethod
    def atualiza_fila(self) -> None:
        AtendimentoPessoas.codigo += 1  # codigo agora é estático
        self.gera_senha_atual()
        AtendimentoPessoas.fila.append(self.senha_atual)  # fila agora é estática
        ...


# Classe AtendimentoAlunos
class AtendimentoAlunos(AtendimentoPessoas):

    def gera_senha_atual(self):
        self.senha_atual = f"A{self.codigo}"

    def atende_pessoa(self, guiche: int) -> str:
        aluno_atual = self.fila.pop(0)
        AtendimentoPessoas.pessoas_atendidas.append(aluno_atual)
        return f"{aluno_atual} - Guichê {guiche}"


class AtendimentoProfessores(AtendimentoPessoas):

    def gera_senha_atual(self):
        self.senha_atual = f"P{self.codigo}"

    def atende_pessoa(self, guiche: int) -> str:
        professor_atual = self.fila.pop(0)
        AtendimentoPessoas.pessoas_atendidas.append(professor_atual)
        return f"Senhor(a) {professor_atual}, dirija-se ao guichê {guiche}"  # tratamento


secretaria_alunos = AtendimentoAlunos()
secretaria_professores = AtendimentoProfessores()

secretaria_alunos.atualiza_fila()
secretaria_alunos.atualiza_fila()

secretaria_professores.atualiza_fila()
secretaria_professores.atualiza_fila()

secretaria_alunos.atualiza_fila()
secretaria_alunos.atualiza_fila()

secretaria_professores.atualiza_fila()
secretaria_professores.atualiza_fila()

print("\t=== Pessoas atualmente na fila:", AtendimentoPessoas.fila)

print(secretaria_alunos.atende_pessoa("3"))
print(secretaria_alunos.atende_pessoa("1"))

print(secretaria_professores.atende_pessoa("2"))
print(secretaria_professores.atende_pessoa("1"))

print("\t=== Pessoas atendidas:", AtendimentoPessoas.pessoas_atendidas)

print("\t=== Pessoas atualmente na fila:", AtendimentoPessoas.fila)
