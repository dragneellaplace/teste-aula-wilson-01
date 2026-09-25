class Cliente:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        self.ativo = True

    def status_matricula(self):
        return f"Cliente {self.nome} está {'Ativo' if self.ativo else 'Inativo'} no plano {self.plano}."

if __name__ == "__main__":
    aluno = Cliente("Ana Silva", "Gold")
    print(aluno.status_matricula())