# TAD posicao

# construtores
def cria_posicao(c, l):  # str x str -> posicao
    """
    Recebe duas cadeias de carateres correspondentes a coluna c
    e a linha l de uma posicao e devolve a posicao correspondente, se ambos os
    argumentos forem validos.
    :param c: Coluna, pode ser 'a', 'b' ou 'c'
    :param l: Linha, pode ser '1', '2' ou '3'
    :return: Posicao do tabuleiro.
    """
    if type(c) != str or type(l) != str:
        raise ValueError('cria posicao: argumentos invalidos')
    if c != 'a' and c != 'b' and c != 'c':
        raise ValueError('cria posicao: argumentos invalidos')
    if l != '1' and l != '2' and l != '3':
        raise ValueError('cria posicao: argumentos invalidos')

    return (c,l)






