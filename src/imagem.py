import polinomio
import mapa
import resolução
import regras

def criar_poli(raizes):
    poli_str = ""
    lista_raizes_str = raizes.split(",")
    for raiz in lista_raizes_str:
        num = str(-complex(raiz))[1:-1]
        if num[0] not in ["+", "-"]:
            num = "+" + num

        poli_str += "(x" + num + ")" + "*"
    
    poli = polinomio.Poli(poli_str[:-1])

    return poli

def criar_lista_raizes(raizes_str):
    raizes = []
    lista_raizes_str = raizes_str.split(",")
    for raiz in lista_raizes_str:
        raizes.append(complex(raiz))

    return raizes

def criar_mapa(raizes):
    print("iniciando calculos")
    rg = regras.Regras(0.1, 100)
    poli = criar_poli(raizes)
    poli.preparar_inicial()
    lista_raizes = criar_lista_raizes(raizes)
    ma = mapa.Mapa(700, 10/700, [0,0], resolução.Newton, poli, lista_raizes, rg)
    ma.gerar_pontos()
    ma.gerar_objetos()
    ma.gerar_cores()
    print("calculos terminados")
    return ma


def gerar_imagem(raizes):
    ma = criar_mapa(raizes)
    print("mapa criado")
    return ma

