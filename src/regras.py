class Regras:
    # armazena regras gerais a serem obedecidas pelos objetos de outras classes
    def __init__(self, prec, maximo, intervalo=None):
        """recebe a precisão, o maximo de iterações e o intervalo da raiz. prec deve ser um float, maximo deve
        ser um int e o intervalo deve ser list com dois elementos float"""
        self.prec = prec
        self.maximo = maximo
        self.intervalo = intervalo
        self.cores_possiveis = [[210,10,10], [10,210,10], [10, 10, 210], [210,210,10], [10,210,210], [210, 10, 210]]
    
    def testar_prec(self, numero, func):
        """testa a precisão de um metodo checando o quão proximo o resultado é do zero. numero deve ser um int
        ou float e func deve ser da classe Func. retorna True se o resultado for mais proximo de zero que a
        precisão estabelecida, senão retorna False"""
        if abs(func(numero)) < self.prec:
            return True
        
        return False