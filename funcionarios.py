class Funcionarios:
    def __init__(self, id, nome, salario) -> None:
        self.id = id
        self.nome = nome
        self.salario = salario
        self.nivel_autorizacao = 5 # 5 -> 1 | 1 é o maior;

class Gerentes(Funcionarios):
    def __init__(self) -> None:
        self.oi = 5
        
    def print_teste(self):
        print(super().__init__())
        

class adm_seguranca(Funcionarios):
    pass
    