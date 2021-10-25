class Func:
    # contem informaçoes referentes a função utilizada
    def __init__(self, conteudo, deriv, deriv2):
        """armazena a função, sua derivada e sua segunda derivada. todos os inputs devem ser da classe function
        e devem receber um unico input int ou float"""
        self.conteudo = conteudo
        self.deriv = deriv
        self.deriv2 = deriv2
    
    def resolver(self, x):
        """chama a função principal e retorna seu resultado para determinado x. o input deve ser int ou float"""
        return self.conteudo(x)