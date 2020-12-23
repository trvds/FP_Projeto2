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
        c = 0
    elif c == 'b':
        c = 1
    elif c == 'c':
        c = 2
    else:
        raise ValueError('cria posicao: argumentos invalidos')

    if l == '1':
        l = 0
    elif l == '2':
        l = 1
    elif l == '3':
        l = 2
    else:
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
    elif j == -1:
        return '[0]'
    elif j == 0:
        return '[ ]'
    else:
        raise ValueError('peca_para_str: argumento invalido')


# Funcoes de alto nivel
def peca_para_inteiro(j):   # peca -> N
    """
    Converte o valor de uma peca para o valor 1, -1 ou 0 dependendo da peca
    :param j: peca
    :return: inteiro com o valor de 1, -1 ou 0 dependendo do valor da peca
    """
    return j


# TAD tabuleiro

# Construtor
def cria_tabuleiro():
    """
    Cria um tabuleiro vazio
    :return: tabuleiro 3x3 vazio
    """
    return [0, 0, 0], [0, 0, 0], [0, 0, 0]


def cria_copia_tabuleiro(t):  # tabuleiro -> tabuleiro
    """

    :param t:
    :return:
    """

    copia = (t[0].copy(), t[1].copy(), t[2].copy())
    return copia


# Seletores
def obter_peca(tab, p):  # tabuleiro x posicao -> peca
    """

    :param tab:
    :param p:
    :return:
    """
    peca = tab[p[0]][p[1]]
    return peca_para_str(peca)


def obter_vetor(tab, sel):  # tabuleiro x str -> tuplo de pecas
    """

    :param tab:
    :param sel:
    :return:
    """
    if sel == 'a':
        sel = 0
    elif sel == 'b':
        sel = 1
    elif sel == 'c':
        sel = 2
    elif sel == '1' or sel == '2' or sel == '3':
        return tuple(tab[int(sel)-1].copy())
    else:
        raise ValueError('obter_vetor: valores invalidos')

    tuplo = ()
    for linha in tab:
        tuplo = tuplo + (linha[sel], )
    return tuplo


# Modificadores
def coloca_peca(tab, peca, pos):  # tabuleiro x peca x posicao -> tabuleiro
    """

    :param tab:
    :param peca:
    :param pos:
    :return:
    """
    tab[pos[0]][pos[1]] = peca
    return tab


def remove_peca(tab, pos):  # tabuleiro x posicao -> tabuleiro
    """

    :param tab:
    :param pos:
    :return:
    """
    tab[pos[0]][pos[1]] = 0
    return tab


def move_peca(tab, pos1, pos2):  # tabuleiro x posicao x posicao -> tabuleiro
    """

    :param tab:
    :param pos1:
    :param pos2:
    :return:
    """
    peca = tab[pos1[0]][pos1[1]]
    tab = coloca_peca(tab, pos2, peca)
    tab = remove_peca(tab, pos1)
    return tab


# Reconhecedor
def eh_tabuleiro(arg):  # universal -> booleano
    """

    :param arg:
    :return:
    """
    x_count = 0
    o_count = 0
    if type(arg) != tuple or len(arg) != 3:
        return False
    for elmts in arg:
        if type(elmt) != list or len(elmt) != 3:
            return False
        for elmt in elmts:
            if elmt == 1:
                x_count += 1
            if elmt == -1:
                o_count += 1
    if o_count != x_count or o_count > 3:
        return False
    return True


def eh_posicao_livre(tab, pos):  # tabuleiro x posicao -> booleano
    """

    :param tab:
    :param pos:
    :return:
    """
    if tab[pos[0]][pos[1]] == 0:
        return True
    return False


# Teste
def tabuleiros_iguais(tab1, tab2):  # tabuleiro x tabuleiro -> booleano
    """

    :param tab1:
    :param tab2:
    :return:
    """
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1 == tab2:
        return True
    return False


# Transformadores
def tabuleiro_para_str(tab):  # tabuleiro -> str
    str(
        posicao_para_str(tab[0][0])+'-'+posicao_para_str(tab[0][1])+'-'+
        posicao_para_str(tab[0][2])
        posicao_para_str(tab[1][0]) + '-' + posicao_para_str(tab[1][1]) + '-' +
        posicao_para_str(tab[1][2])
        posicao_para_str(tab[2][0]) + '-' + posicao_para_str(tab[2][1]) + '-' +
        posicao_para_str(tab[2][2]))
