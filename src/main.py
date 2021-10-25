import implementar_interface as ii
import regras
import func
import mapa
import resolução

def main():
    rg = regras.Regras(0.1, 100000)
    fu = func.Func(lambda x: (x+2)*(x+2j)*(x-2j)*(x-2-1j)*(x+2+1j), lambda x: 5*x**4 + 8*x**3 + (3-12j)*x**2 + (4-16j)*x - (12+16j), None)
    ma = mapa.Mapa(700, 10/700, [0,0], resolução.Newton, fu, [-2, -2-1j, -2j, 2j, 2+1j], rg)
    ma.gerar_pontos()
    ma.gerar_objetos()
    ma.gerar_cores()
    print("calculso concluidos")
    interface = ii.main(ma)
    interface.main_loop()

if __name__ == "__main__":
    main()
