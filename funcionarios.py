class Funcionarios:
    def __init__(self, id, nome, idade, salario) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.idade = idade

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Salário: {self.salario:.2f}"


class Gerente(Funcionarios):
    def __init__(self, id, nome, idade, salario) -> None:
        super().__init__(id, nome, idade, salario)
        self.nivel_autorizacao = 3  # Nível máximo de autorização

    def __str__(self):
        detalhes = super().__str__()
        return f"{detalhes} | Nível de Autorização: {self.nivel_autorizacao}"


class Adm_Seguranca(Funcionarios):
    def __init__(self, id, nome, idade, salario) -> None:
        super().__init__(id, nome, idade, salario)
        self.nivel_autorizacao = 2  # Nível médio de autorização

    def __str__(self):
        detalhes = super().__str__()
        return f"{detalhes} | Nível de Autorização: {self.nivel_autorizacao}"


class Diretor(Funcionarios):
    def __init__(self, id, nome, idade, salario) -> None:
        super().__init__(id, nome, idade, salario)
        self.nivel_autorizacao = 1  # Nível mais alto de autorização

    def __str__(self):
        detalhes = super().__str__()
        return f"{detalhes} | Nível de Autorização: {self.nivel_autorizacao}"

