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

    return c, l


def cria_copia_posicao(p):  # posicao -> posicao
    """
    Permite criar uma copia de uma posicao
    :param p: posicao
    :return: posicao
    """
    if not eh_posicao(p):
        raise ValueError('cria posicao: argumentos invalidos')

    return p


# Seletores
def obter_pos_c(p):  # posicao -> str
    """
    Permite obter a coluna de uma posicao.
    :param p: posicao
    :return: coluna da posicao
    """
    return p[0]


def obter_pos_l(p):  # posicao -> str
    """
    Permite obter a linha de uma posicao.
    :param p: posicao
    :return: linha da posicao
    """
    return p[1]


# Reconhecedores
def eh_posicao(p):  # universal -> booleano
    """
    Indica se certo argumento e uma posicao ou nao
    :param p: posicao
    :return: True se o argumento for uma posicao, False caso contrario
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
def posicoes_iguais(p1, p2):  # posicao x posicao -> booleano
    """
    Indica se as posicoes inseridas sao iguais
    :param p1: posicao
    :param p2: posicao
    :return: True se as posicoes forem iguais, False caso contrario
    """
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    if p1 != p2:
        return False
    return True


# Transformador
def posicao_para_str(p):  # posicao -> str
    """
    Transforma a posicao numa string
    :param p: posicao
    :return: string com a posicao
    """
    return p[0]+p[1]


# Funcoes de alto nivel

def obter_posicoes_adjacentes(p):  # posicao -> tuplo de posicoes
    """
    Indica as posicoes adjacentes a posicao introduzida
    :param p: posicao
    :return: tuplo com as posicoes adjacentes
    """

    return 0