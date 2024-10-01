class Funcionarios:
    def __init__(self, id, nome, salario) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.nivel_autorizacao = 5 # 5 -> 1 | 1 é o maior;

class Gerentes(Funcionarios):
    def __init__(self) -> None:
        pass

class adm_seguranca(Funcionarios):
    pass

class diretor(Funcionarios):
    def __init__(self, id, nome, salario) -> None:
        super().__init__(id, nome, salario)
    