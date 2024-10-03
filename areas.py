# Criação dos objetos que representam as áreas da empresa

class Area:
    def __init__(self, nome, nivel_acesso, capacidade_maxima):
        self.nome = nome
        self.nivel_acesso = nivel_acesso
        self.capacidade_maxima = capacidade_maxima
        self.ocupacao_atual = 0 

    def permitir_acesso(self, usuario):
        if usuario.nivel_acesso < self.nivel_acesso:
            return f"Acesso negado para {usuario.nome} na {self.nome}."
        
        if self.ocupacao_atual >= self.capacidade_maxima:
            return f"Acesso negado: {self.nome} está com a capacidade máxima de {self.capacidade_maxima} pessoas."
        
        self.ocupacao_atual += 1
        return f"Acesso permitido para {usuario.nome} na {self.nome}."

    def sair(self, usuario):
        if self.ocupacao_atual > 0:
            self.ocupacao_atual -= 1
            return f"{usuario.nome} saiu da {self.nome}."
        else:
            return f"Erro: Nenhuma pessoa dentro da {self.nome}."

class AreaComum(Area):
    def __init__(self):
        super().__init__(nome="Área Comum", nivel_acesso=1, capacidade_maxima=50)

class Laboratorio(Area):
    def __init__(self):
        super().__init__(nome="Laboratório de P&D", nivel_acesso=2, capacidade_maxima=10)

class SalaControle(Area):
    def __init__(self):
        super().__init__(nome="Sala de Controle de Segurança", nivel_acesso=3, capacidade_maxima=5)

class Cofre(Area):
    def __init__(self):
        super().__init__(nome="Cofre Principal", nivel_acesso=3, capacidade_maxima=2)