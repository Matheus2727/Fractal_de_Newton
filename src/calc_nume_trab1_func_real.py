import matplotlib.pyplot as plt
# importa "matplotlib.plt" para plotar os graficos

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

class Regras:
    # armazena regras gerais a serem obedecidas pelos objetos de outras classes
    def __init__(self, prec, maximo, intervalo=None):
        """recebe a precisão, o maximo de iterações e o intervalo da raiz. prec deve ser um float, maximo deve
        ser um int e o intervalo deve ser list com dois elementos float"""
        self.prec = prec
        self.maximo = maximo
        self.intervalo = intervalo
    
    def testar_prec(self, numero, func):
        """testa a precisão de um metodo checando o quão proximo o resultado é do zero. numero deve ser um int
        ou float e func deve ser da classe Func. retorna True se o resultado for mais proximo de zero que a
        precisão estabelecida, senão retorna False"""
        if abs(func.resolver(numero)) < self.prec:
            return True
        
        return False

class Raizes:
    # contem metodos para checar se existem raizes no intervalo
    def __init__(self, func, intervalo):
        """func deve ser da classe Func, intervalodeve ser uma list com 2 elementos int ou float"""
        self.func = func
        self.intervalo = intervalo

    def bolzano(self):
        """executa o metodo de bolzano pra checar se existe um numero par de raizes no intervalo, retorna False
        se o numero de raizes for impar e True se for par"""
        cons_sinal = self.func.resolver(self.intervalo[0]) * self.func.resolver(self.intervalo[1]) # multiplica os valores nas extremidades do intervalo
        pos = True
        if cons_sinal < 0: #checa se o procuto é negativo
            pos = False
        
        elif cons_sinal > 0:
            pos = True
        
        else: # se o produto for zero não sera necessario usar metodos pra determinar as raizes
            print("um dos dois é raiz {0}".format(self.intervalo))
        
        return pos
    
    def teste_deriv(self):
        """realiza o teste da derivada pra determinar se a derivada muda de sinal no intervalo, retornando
        True se muda"""
        testes = regras.maximo # usa o numero maximo de iteraçoes como base pro numero de testes
        distancia = self.intervalo[1] - self.intervalo[0] # a distancia entre os extremos do intervalo
        passo = distancia / testes # o tamanho passo a ser tomado entre um ponto e outro
        sinal = ""
        muda = False
        for i in range(testes + 1): # realizar testes+1 operaçoes, o primeira teste no primeiro extremo do intervalo, o ultimo teste no ultimo
            resultado = self.func.deriv(self.intervalo[0] + passo * i) # o valor da derivada no ponto
            if resultado >= 0: #checa o sinal
                sinal_atual = "+"
            
            elif resultado <= 0:
                sinal_atual = "-"
            
            if sinal == "":
                sinal = sinal_atual
            
            elif sinal != sinal_atual:
                muda = True
                break
        
        return muda
    
    def conclu(self):
        """printa na tela as conclusões obtidas pelos metodos acima"""
        if not self.bolzano():
            print("por bolzano ha um numero impar de raizes no intervalo")
    
        else:
            print("por bolzano ha um numero par de raizesno intervalo")

        if not self.teste_deriv():
            print("o sinal da derivada não muda no intervalo")
        
        else:
            print("o sinal da derivada muda no intervalo")

class Newt:
    # contem o passo a passo do metodo de newton para achar a raize de uma função num dado intervalo
    def __init__(self, func, intervalo):
        """recebe as informaçoes iniciais. func é um objeto da classe Func e o intervalo deve ser list ou
        tuple com 2 elementos int ou float"""
        self.func = func
        self.intervalo = intervalo
        self.x0 = "" # o valor x atual onde sera aplicado o metodo de newton
        self.tent = 0 # o numero de iteraçoes executadas ate o momento
        self.resultado = "" # o valor aproximado da raiz dentro da tolerancia (ou um valor qualquer fora do intervalo no caso de um erro)
        self.resultado_final = "" # o self.resultado e o self.tent em uma tupla
        self.prec = "" # e output do ultimo teste de precisão realisado

    def loop(self):
        """o loop principal, cada vez que for rodado aumentará em um o numero de iteraçoes. ele se encerra
        com um bom resultado se self.precisão for True. tambem se encerra se o numero maximo de iteraçoes
        for alcançado, se a derivada em algum ponto é zero ou se o ponto x0 sair do intervalo, tendo assim
        um resultado não ideal"""
        while self.tent < regras.maximo and not self.prec: # checa a precisão da iteração anterior e o numero atual de iterações
            self.tent += 1 # aumenta a iteração
            func = self.func.resolver(self.x0) # o resultado da função no ponto
            deriv = self.func.deriv(self.x0) # o resultado da derivada no ponto
            if deriv == 0: # filtrando o erro de "dividir por zero"
                print("{} na derivada é zero".format(self.x0))
                break

            self.x0 = self.x0 - func / deriv # escolhendo um novo x0
            self.prec = regras.testar_prec(self.x0, self.func) # teste de precisão do novo x0
            if self.x0 <= self.intervalo[0] or self.x0 >= self.intervalo[1]: # teste se o x0 esta fora do intervalo
                print("{} esta fora do intervalo".format(self.x0))
                break
        
        self.resultado = self.x0 # armazenando o resultado do loop (ideal ou n)
        self.resultado_final = self.resultado, self.tent # formato a ser apresentado como resposta
    
    def escolher_x0(self):
        """seleciona um ponto pra ser o x0 inicial, esse ponto esta no meio do intervalo"""
        dist = (self.intervalo[1] - self.intervalo[0]) / 2
        self.x0 = self.intervalo[0] + dist
    
    def start(self):
        """inicia o passo a passo pra obter um resultado"""
        self.escolher_x0()
        self.loop()
    
    def resultado_fin(self):
        return self.resultado_final

class Grafico:
    # armazena as informaçoes e metodos para gerar um grafico do problema
    def __init__(self, func):
        """recebe um objeto Func e seta um intervalo teorico inicial"""
        self.func = func
        self.intervalo = [-10, 10]

    def plotar(self):
        """plota a função dada no intervalo dado"""
        x = [self.intervalo[0]] # o primeiro x é o primeiro elemento do intervalo
        y = [self.func.resolver(x[-1])] # cada y é afunção aplicada ao ultimo x gerado
        dist = abs(self.intervalo[1]-self.intervalo[0])
        for _ in range(regras.maximo): # gera um x1 a partir do x0 gerando anteriormente somando esse x0 a um passo, repetindo esse loop para o maximo de iteraçoes
            x.append(x[-1] + dist / regras.maximo)
            y.append(self.func.resolver(x[-1]))

        _, ax = plt.subplots()
        ax.plot(x, y) # plota a lista de valores num grafico
        ax.set(xlabel='x', ylabel='y', title='grafico')
        ax.grid()
        plt.show()

    def loop_grafico(self):
        """possibilita o refino do intervalo inicial em um loop de interaçoes com o usuario
        pelo terminal"""
        intervalo = self.intervalo
        while True: # loop que quebra quando o usuario digita "sair"
            escolha = input("escolha um intervalo formato: x1,x2 ou digite sair: ") # armazena um intervalo ou a palavra sair
            if escolha == "sair":
                break

            s1, s2 = escolha.split(",") # formata o intervalo do usuario
            self.intervalo = [float(s1), float(s2)]
            self.plotar() # plota o grafico no intervalo

def setarFunc():
    """cria um objeto Func com os dados obtidos na mão, retorna esse objeto"""
    const = 8.987 * 10**(9) * 5 * 10**(-12)
    f1 = lambda x : const * (3/x - 3/(((5 * 10**(-2))**2 + x**2)**(1/2))) - 0.005 # função do problema modelado
    f2 = lambda x : const * (-3/x**2 + (3 * x)/(1/400 + x**2)**(3/2)) # derivada da função anterior
    f3 = lambda x : const * (6/x**3 - (9 * x**2)/(1/400 + x**2)**(5/2) + 3/(1/400 + x**2)**(3/2)) # derivada segunda da função inicial
    func = Func(f1, f2, f3)
    return func
    
def achar_raizes(func):
    """realiza os metodos da classe Raizes na func dada e no intervalo escolhido nas regras. func é um objeto da classe Func"""
    raizes = Raizes(func, regras.intervalo)
    raizes.conclu()

def iniciar_metodo(func):
    """inicia um objeto da classe um metodo pra func dada, retorna esse objeto (no caso o metodo de newton).
    func é um objeto da classe Func"""
    newt = Newt(func, regras.intervalo)
    return newt

def testar():
    """inicia os calculos do metodo iniciado"""
    metodo.start()

def mostrar():
    """coleta os resultados do metodo e formata para ser printado ou exportado pra interface"""
    resultado = str(metodo.resultado_fin()).split(",")
    texto = "Newt:\n"
    texto += "raiz: " +  resultado[0][1:] + " iterações: "  + resultado[1][:-1] + "\n"
    return texto


def main():
    """a função principal, quando chamada roda o programa, deixando os resultados preparados para serem obtidos"""
    global regras
    global grafico
    global metodo
    global raizes
    regras = Regras(0.000001, 2000) # inicia as regras a serem seguidas nesse programa
    func = setarFunc() # cria um objeto de Func com a função a ser usada
    grafico = Grafico(func) # prepara um objeto de Grafico para plotar se necessario
    grafico.intervalo = [0.1, 0.5] # um intervalo obtido experimentalmente onde é possivel ver a interseção da função com o eixo quando plotado
    regras.intervalo = [0.3,0.35] # um intervalo obtido pelo metodo grafico, checado pelo teorema de bolzado e pelometodo da derivada
    raizes = Raizes(func, regras.intervalo)
    metodo = iniciar_metodo(func) # inicia um objeto Newt
    testar() # executa as contas do metodo de newton

main()

if __name__ == "__main__":
    print(mostrar()) # se o programa não estiver sendo importado printa os resultados no terminal
    raizes.conclu()
    input()


