from datetime import datetime



class Pessoa():
    def __init__(self, nome, ano_denacimento):
        self.nome = nome
        self.ano_nascimento = ano_denacimento

    def calcular_idade(self):
        ano_atual = datetime.now().year
        self.idade = ano_atual - self.ano_nascimento
        return self.idade

    def maior_18 (self):
        if self.idade >= 18:
            return f"{self.nome} tem {self.idade} ja é maior de idade"
        else:
            return f"{self.nome} tem {self.idade} nao é maior de idade"


