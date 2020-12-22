# TAD posicao

# Construtores
def cria_posicao(c, l):  # str x str -> posicao
    """
    Recebe duas cadeias de carateres correspondentes a coluna c
    e a linha l de uma posicao e devolve a posicao correspondente, se ambos os
    argumentos forem validos.
    :param c: Coluna, pode ser 'a', 'b' ou 'c'
    :param l: Linha, pode ser '1', '2' ou '3'
    :return: Posicao do tabuleiro.
    """

    p = [c, l]
    if not eh_posicao(p):
        raise ValueError('cria posicao: argumentos invalidos')

    return (c,l)


def cria_copia_posicao(p):
    """

    :param p:
    :return:
    """
    if not eh_posicao(p):
        raise ValueError('cria posicao: argumentos invalidos')

    return p


# Seletores
def obter_pos_c(p):
    """

    :param p:
    :return:
    """
    return p[0]


def obter_pos_l(p):
    """

    :param p:
    :return:
    """
    return p[1]


# Reconhecedores
def eh_posicao(p):
    """

    :param p:
    :return:
    """
    c = p[0]
    l = p[1]

    if type(c) != str or type(l) != str:
        return False
    if c != 'a' and c != 'b' and c != 'c':
          return False
    if l != '1' and l != '2' and l != '3':
        return False

    return True


# Teste
def posicoes_iguais(p1, p2):
    """

    :param p1:
    :param p2:
    :return:
    """
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    if p1 != p2:
        return False
    return True


# Transformador
def posicao_para_str(p):
    """

    :param p:
    :return:
    """
    return p[0]+p[1]


# Funcoes de alto nivel

def obter_posicoes_adjacentes():
