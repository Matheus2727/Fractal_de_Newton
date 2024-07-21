import interface
import imagem


def exemplo(**kwargs):
    """exemplo de função para ser usada em um botao"""
    print("a")


def localizar(janela, nome:str):
    conteudo = ""
    for input in janela.inputs:
        if input.nome == nome:
            conteudo = input.input

    return conteudo


def preparar_imagem(**kwargs):
    janela = kwargs["janela"]
    nome = "raizes"
    raizes = localizar(janela, nome)
    ma = imagem.gerar_imagem(raizes)
    setarquads(janela, ma, raizes)


def limpar(**kwargs):
    janela = kwargs["janela"]
    nome = "raizes"
    conteudo = ""
    for input in janela.inputs:
        if input.nome == nome:
            input.input = conteudo
            input.cursor = 0


def setarbots(janela: interface.Janela):
    """seta os botoes e os adiciona a janela"""
    bot_atualizar = interface.Botao(20, 90, 0, 0, "atualizar", "", 30, [120, 120, 120], preparar_imagem, {"janela": janela})
    bot_limpar = interface.Botao(230, 90, 0, 0, "limpar", "", 30, [120, 120, 120], limpar, {"janela": janela})
    janela.addBotões([bot_atualizar, bot_limpar])


def setartextos(janela: interface.Janela):
    """seta os textos e os adiciona a janela"""
    text_func = interface.Texto(10, 10, 30, "função:", "")
    text_raizes = interface.Texto(20, 50, 30, "raizes:", "")
    janela.addTextos([text_func, text_raizes])


def setarinputs(janela: interface.Janela):
    """seta os inputs e os adiciona a janela"""
    inpu_raizes = interface.Inp(130, 50, 10, 30, "1,1j,-2,3-1j,-2j", "raizes")
    janela.addInputs([inpu_raizes])


def setarquads(janela: interface.Janela, mapa, raizes):
    """seta os quadrados (pixels da imagem) e os adiciona a janela"""
    print("iniciando imagem")
    cons = 1
    quads = []
    for il, linha in enumerate(mapa.cores):
        for ic, cor in enumerate(linha):
            quads.append(interface.Quadrado(ic, il, cons, cor))

    print("imagem pronta")
    janela.salvar_imagem(quads, raizes)


def main():
    """cria um objeto Janela, organiza os botoes, textos e inputs.
    Apos isso seta os valores iniciais"""
    janela = interface.Janela(700, 700, "menu")
    setarbots(janela)
    setartextos(janela)
    setarinputs(janela)
    janela.iniciar()
    return janela


if __name__ == "__main__":
    main()
