from regras import Regras


class Newton:
    # contem o passo a passo do metodo de newton para achar a raize de uma função
    def __init__(self, func, regras, x0:complex=None):
        """recebe as informaçoes iniciais. func é um objeto da classe Poli, regras é um objeto Regras,
        e x0 é o x inicial"""
        self.func = func
        self.x0 = "" # o valor x atual onde sera aplicado o metodo de newton
        self.tent = 0 # o numero de iteraçoes executadas ate o momento
        self.resultado = "" # o valor aproximado da raiz dentro da tolerancia (ou um valor qualquer fora do intervalo no caso de um erro)
        self.resultado_final = "" # o self.resultado e o self.tent em uma tupla
        self.prec = "" # e output do ultimo teste de precisão realisado
        self.regras = regras
        self.x0 = x0

    def loop(self):
        """o loop principal, cada vez que for rodado aumentará em um o numero de iteraçoes. ele se encerra
        com um bom resultado se self.precisão for True. tambem se encerra se o numero maximo de iteraçoes
        for alcançado, se a derivada em algum ponto é zero ou se o ponto x0 sair do intervalo, tendo assim
        um resultado não ideal"""
        while self.tent < self.regras.maximo and not self.prec: # checa a precisão da iteração anterior e o numero atual de iterações
            self.tent += 1 # aumenta a iteração
            func = self.func(self.x0) # o resultado da função no ponto
            deriv = self.func.resolver(self.func.derivada, self.x0) # o resultado da derivada no ponto
            if deriv == 0: # filtrando o erro de "dividir por zero"
                print("{} na derivada é zero".format(self.x0))
                break

            self.x0 = self.x0 - func / deriv # escolhendo um novo x0
            self.prec = self.regras.testar_prec(self.x0, self.func) # teste de precisão do novo x0
        
        self.resultado = self.x0 # armazenando o resultado do loop (ideal ou n)
        self.resultado_final = self.resultado, self.tent # formato a ser apresentado como resposta
    
    def start(self):
        """inicia o passo a passo pra obter um resultado"""
        self.loop()
    
    def resultado_fin(self):
        return self.resultado_final
