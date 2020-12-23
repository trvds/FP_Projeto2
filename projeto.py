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
    if c == 'a':
        c = 1
    elif c == 'b':
        c = 2
    elif c == 'c':
        c = 3
    else:
        raise ValueError('cria posicao: argumentos invalidos')

    l = int(l)
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
    if p[0] == 1:
        return '1'
    elif p[0] == 2:
        return '2'
    elif p[0] == 3:
        return '3'
    else:
        raise ValueError('obter_pos_c: argumento invalido')


def obter_pos_l(p):  # posicao -> str
    """
    Permite obter a linha de uma posicao.
    :param p: posicao
    :return: linha da posicao
    """
    return str(p[1])


# Reconhecedores
def eh_posicao(p):  # universal -> booleano
    """
    Indica se certo argumento e uma posicao ou nao
    :param p: posicao
    :return: True se o argumento for uma posicao, False caso contrario
    """
    c = p[0]
    l = p[1]

    if type(c) != int or type(l) != int:
        return False
    if c != '1' and c != '2' and c != '3':
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


# TAD peca

# Construtor
def cria_peca(s):  # str -> peca
    """
    Recebe uma cadeia de carateres correspondentea uma peca e devolve a peca
    correspondente se o argumento for valido.
    :param s: String da peca (pode ser 'X', 'O' ou ' ')
    :return: peca
    """
    if s == 'X':
        return 1
    elif s == 'O':
        return -1
    elif s == ' ':
        return 0
    else:
        raise ValueError('cria peca: argumento invalido')


def cria_copia_peca(j):  # peca -> peca
    """
    Permite copiar uma peca.
    :param j: peca
    :return: valor da peca
    """
    if not eh_peca(j):
        return ValueError
    return j


# Reconhecedor
def eh_peca(arg):   # universal -> booleano
    """
    Indica se determinado argumento e uma peca
    :param arg: valor da peca
    :return: True se o argumento for uma peca, False caso contrario
    """
    if type(arg) != int:
        return False
    if arg != 1 and arg != -1 and arg != 0:
        return False
    return True


# Teste
def pecas_iguais(j1, j2):   # peca x peca -> booleano
    """
    Indica se duas pecas sao iguais
    :param j1: peca 1
    :param j2: peca 2
    :return: True se forem iguais, False caso contrario
    """
    if j1 == j2:
        return True
    return False


# Transformador
def peca_para_str(j):  # peca -> str
    """

    :param j:
    :return:
    """
    if j == 1:
        return '[X]'
    elif j == 1:
        return '[0]'
    elif j == 0:
        return '[ ]'
    else:
        raise ValueError('peca_para_str: argumento invalido')


# Funcoes de alto nivel
def peca_para_inteiro(j):
    """
    Converte o valor de uma peca para inteiro
    :param j: peca
    :return: inteiro com o valor de 1, -1 ou 0 dependendo do valor da peca
    """
    return j