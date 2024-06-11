class Senha():
    def __init__(self, conteudo):
        self.senha = conteudo
    def inserir_senha(self, senha):
        if self.senha < 10:
            print('Por favor, colocar no minimo 10 caracteres')
        elif self.senha < 30:
            print('Por favor, colocar no máximo 30 caracteres')
        else:
            lista_senha = []
            lista_senha.append(self.senha)
