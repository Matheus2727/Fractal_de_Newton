import interface


def exemplo(**kwargs):
    """exemplo de função para ser usada em um botao"""
    print("a")


def setarquads(janela: interface.Janela, mapa):
    """ideia de função para criar e adicionar botoes"""
    print("iniciando imagem")
    cons = 1
    quads = []
    for il, linha in enumerate(mapa.cores):
        for ic, cor in enumerate(linha):
            quads.append(interface.Quadrado(ic, il, cons, cor))

    print("imagem pronta")
    janela.addQuads(quads)


def main(mapa):
    """cria um objeto Janela, organiza os botoes, textos e inputs.
    Apos isso seta os valores iniciais"""
    janela = interface.Janela(700, 700, "menu")
    setarquads(janela, mapa)
    janela.iniciar()
    return janela


if __name__ == "__main__":
    main()
