class Mapa:
    def __init__(self, dim:int, escala:float, offset:list, classe, func, raizes, regras):
        """recebe as dimensoes do mapa (numero de linhas), uma constante
        a qual sera multiplicada pelos indices dos pontos, uma lista com
        dois float representando o deslocamento a partir da origem, a
        classe a ser usada na resolução dos pontos, a função em questao, 
        as raizes dessa função e um objeto Regras"""
        self.dim = dim
        self.escala = escala
        self.raizes = raizes
        self.pontos = None
        self.res = None
        self.cores = None
        self.raizes_cores = None
        self.offset = offset
        self.classe = classe
        self.func = func
        self.regras = regras
    
    def gerar_pontos(self):
        pontos = []
        for l in range(self.dim):
            nova_linha = []
            for c in range(self.dim):
                coord = []
                coord.append(c*self.escala + (-self.dim//2 + self.offset[0])*self.escala)
                coord.append(-l*self.escala + (+self.dim//2 + self.offset[1])*self.escala)
                
                nova_linha.append(coord)
            
            pontos.append(nova_linha)
        
        self.pontos = pontos
    
    def gerar_objetos(self):
        res = []
        for l in range(self.dim):
            nova_linha = []
            for c in range(self.dim):
                ponto = self.pontos[l][c][0] + self.pontos[l][c][1]*1j
                objeto = self.classe(self.func, self.regras, ponto)
                objeto.loop()
                nova_linha.append(objeto.resultado)
            
            res.append(nova_linha)
        
        self.res = res
    
    def gerar_cores(self):
        self.raizes_cores = {}
        for i, x in enumerate(self.raizes):
            self.raizes_cores[x] = self.regras.cores_possiveis[i]

        cores = []
        for l in range(self.dim):
            nova_linha = []
            for c in range(self.dim):
                distancias = []
                re = self.res[l][c]
                for r in self.raizes:
                    distancias.append(abs(re-r))
                
                menor_distancia = min(distancias)
                for i, d in enumerate(distancias):
                    if d == menor_distancia:
                        nova_linha.append(self.raizes_cores[self.raizes[i]])
                        break
            
            cores.append(nova_linha)
        
        self.cores = cores
