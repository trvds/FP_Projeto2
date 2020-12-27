# TAD posicao-------------------------------------------------------------------

# Construtores
def obter_str_colunas():  # {} -> tuplo com strings das colunas
    """

    :return:
    """
    return 'a', 'b', 'c'


def obter_str_linhas():  # {} -> tuplo com strings das colunas
    """

    :return:
    """
    return '1', '2', '3'


def cria_posicao(c, ln):  # str x str -> posicao
    """
    Recebe duas cadeias de carateres correspondentes a coluna c
    e a linha l de uma posicao e devolve a posicao correspondente, se ambos os
    argumentos forem validos.
    :param c: Coluna, pode ser 'a', 'b' ou 'c'
    :param ln: Linha, pode ser '1', '2' ou '3'
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

    if ln == '1':
        ln = 0
    elif ln == '2':
        ln = 1
    elif ln == '3':
        ln = 2
    else:
        raise ValueError('cria posicao: argumentos invalidos')

    return c, ln


def cria_copia_posicao(p):  # posicao -> posicao
    """
    Permite criar uma copia de uma posicao
    :param p: posicao
    :return: posicao
    """
    if not eh_posicao(p):
        raise ValueError('cria posicao: argumentos invalidos')
    pos = cria_posicao(p[0], p[1])
    return pos


# Seletores
def obter_pos_c(p):  # posicao -> str
    """
    Permite obter a coluna de uma posicao.
    :param p: posicao
    :return: coluna da posicao
    """
    if p[0] == 0:
        return 'a'
    elif p[0] == 1:
        return 'b'
    elif p[0] == 2:
        return 'c'
    else:
        raise ValueError('obter_pos_c: argumento invalido')


def obter_pos_l(p):  # posicao -> str
    """
    Permite obter a linha de uma posicao.
    :param p: posicao
    :return: linha da posicao
    """
    if p[1] == 0:
        return '1'
    elif p[1] == 1:
        return '2'
    elif p[1] == 2:
        return '3'
    else:
        raise ValueError('obter_pos_c: argumento invalido')


# Reconhecedores
def eh_posicao(p):  # universal -> booleano
    """
    Indica se certo argumento e uma posicao ou nao
    :param p: posicao
    :return: True se o argumento for uma posicao, False caso contrario
    """
    c = p[0]
    ln = p[1]
    if type(c) != int or type(ln) != int:
        return False
    if c != 0 and c != 1 and c != 2:
        return False
    if ln != 0 and ln != 1 and ln != 2:
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
def posicao_para_str(pos):  # posicao -> str
    """
    Transforma a posicao numa string
    :param pos: posicao
    :return: string com a posicao
    """
    return obter_pos_c(pos) + obter_pos_l(pos)


def cl_adjacente(cl, fn):
    """

    :param cl:
    :param fn:
    :return:
    """
    if cl == 'a':
        cl = 0
    elif cl == 'b':
        cl = 1
    elif cl == 'c':
        cl = 2
    if cl == '1':
        cl = 0
    elif cl == '2':
        cl = 1
    elif cl == '3':
        cl = 2
    if 0 <= fn(cl) <= 2:
        return fn(cl)
    return False


# Funcoes de alto nivel---------------------------------------------------------
def obter_posicoes_adjacentes(pos):  # posicao -> tuplo de posicoes
    """
    Indica as posicoes adjacentes a posicao introduzida
    :param pos: posicao
    :return: tuplo com as posicoes adjacentes
    """
    posicoes = ()
    col = obter_pos_c(pos)
    ln = obter_pos_l(pos)
    if type(cl_adjacente(ln, lambda x: x-1)) == int:
        posicoes += (cl_adjacente(col, lambda x: x),
                     cl_adjacente(ln, lambda x: x-1)),
    if type(cl_adjacente(col, lambda x: x-1)) == int:
        posicoes += (cl_adjacente(col, lambda x: x-1),
                     cl_adjacente(ln, lambda x: x)),
    if type(cl_adjacente(col, lambda x: x+1)) == int:
        posicoes += (cl_adjacente(col, lambda x: x+1),
                     cl_adjacente(ln, lambda x: x)),
    if type(cl_adjacente(ln, lambda x: x+1)) == int:
        posicoes += (cl_adjacente(col, lambda x: x),
                     cl_adjacente(ln, lambda x: x+1)),
    return posicoes


# TAD peca----------------------------------------------------------------------

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
def eh_peca(arg):  # universal -> booleano
    """
    Indica se determinado argumento e uma peca
    :param arg: valor da peca
    :return: True se o argumento for uma peca, False caso contrario
    """
    if type(arg) == int:
        if arg == 1 or arg == -1 or arg == 0:
            return True
    return False


# Teste
def pecas_iguais(j1, j2):  # peca x peca -> booleano
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


# Funcoes de alto nivel---------------------------------------------------------
def peca_para_inteiro(peca):  # peca -> N
    """
    Converte o valor de uma peca para o valor 1, -1 ou 0 dependendo da peca
    :param peca: peca
    :return: inteiro com o valor de 1, -1 ou 0 dependendo do valor da peca
    """
    if pecas_iguais(cria_peca(' '), peca):
        return 0
    elif pecas_iguais(cria_peca('X'), peca):
        return 1
    elif pecas_iguais(cria_peca('O'), peca):
        return -1
    else:
        return ValueError('peca_para_inteiro: argumento nao e uma peca')


# TAD tabuleiro-----------------------------------------------------------------

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
    peca = tab[p[1]][p[0]]
    return peca


def obter_vetor(tab, sel):  # tabuleiro x str -> tuplo de pecas
    """

    :param tab:
    :param sel:
    :return:
    """
    if sel == '1' or sel == '2' or sel == '3':
        sel = int(sel) - 1
        return tuple(tab[sel])
    elif sel == 'a':
        sel = 0
    elif sel == 'b':
        sel = 1
    elif sel == 'c':
        sel = 2
    else:
        raise ValueError('obter_vetor: valores invalidos')
    tuplo = ()
    for linha in tab:
        tuplo = tuplo + (linha[sel],)
    return tuplo


# Modificadores
def coloca_peca(tab, peca, pos):  # tabuleiro x peca x posicao -> tabuleiro
    """

    :param tab:
    :param peca:
    :param pos:
    :return:
    """
    tab[pos[1]][pos[0]] = peca
    return tab


def remove_peca(tab, pos):  # tabuleiro x posicao -> tabuleiro
    """

    :param tab:
    :param pos:
    :return:
    """
    tab[pos[1]][pos[0]] = 0
    return tab


def move_peca(tab, pos1, pos2):  # tabuleiro x posicao x posicao -> tabuleiro
    """

    :param tab:
    :param pos1:
    :param pos2:
    :return:
    """
    peca = tab[pos1[1]][pos1[0]]
    tab = coloca_peca(tab, peca, pos2)
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
        if type(elmts) != list or len(elmts) != 3:
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
    if tab[pos[1]][pos[0]] == 0:
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
    """

    :param tab:
    :return:
    """
    tabstr = '   a   b   c \n'
    for linha in range(3):
        tabstr += str(linha + 1)+' '
        for coluna in range(3):
            tabstr += peca_para_str(tab[linha][coluna])
            if coluna < 2:
                tabstr += '-'
            else:
                tabstr += '\n'
        if linha < 2:
            tabstr += '   | \ | / | \n'
    return tabstr


def tuplo_para_tabuleiro(tuplo):  # tuplo -> tabuleiro
    """

    :return:
    """
    return list(tuplo[0]), list(tuplo[1]), list(tuplo[2])


# Funcoes de alto nivel---------------------------------------------------------
def obter_ganhador(tab):  # tabuleiro -> peca
    """

    :param tab:
    :return:
    """
    x = cria_peca('X')
    o = cria_peca('O')
    livre = cria_peca(' ')
    indices = ('1', '2', '3', 'a', 'b', 'c')

    for indice in indices:
        vetor = obter_vetor(tab, indice)
        if vetor == (x, x, x):
            return x
        if vetor == (o, o, o):
            return o
    return livre


def obter_posicoes_livres(tab):  # tabuleiro -> tuplo de posicoes
    """

    :param tab:
    :return:
    """
    colunas = obter_str_colunas()
    linhas = obter_str_linhas()
    posicoes = ()
    for linha in linhas:
        for coluna in colunas:
            if pecas_iguais(obter_peca(tab, cria_posicao(coluna, linha)),
                            cria_peca(' ')):
                posicoes += (cria_posicao(coluna, linha),)
    return posicoes


def obter_posicoes_jogador(tab, peca):  # tabuleiro x peca -> tuplo de posicoes
    """

    :param tab:
    :param peca:
    :return:
    """
    colunas = obter_str_colunas()
    linhas = obter_str_linhas()
    posicoes = ()
    for linha in linhas:
        for coluna in colunas:
            if pecas_iguais(obter_peca(tab, cria_posicao(coluna, linha)), peca):
                posicoes += (cria_posicao(coluna, linha),)
    return posicoes


# Funcoes adicionais------------------------------------------------------------
def obter_movimento_manual(tab, peca):  # tabuleiro x peca -> tuplo de posicoes
    """

    :param tab:
    :param peca:
    :return:
    """
    if peca == cria_peca('X') or peca == cria_peca('O'):
        if conta_peca(tab, peca) < 3:
            pos = str(input('Turno do jogador. Escolha uma posicao: '))
            if len(pos) == 2 and type(pos) == str:
                pos = cria_posicao(pos[0], pos[1])
                if eh_posicao_livre(tab, pos):
                    return pos,
        if conta_peca(tab, peca) == 3:
            pos = str(input('Turno do jogador. Escolha um movimento: '))
            if len(pos) == 4 and type(pos) == str:
                pos1 = cria_posicao(pos[0], pos[1])
                pos2 = cria_posicao(pos[2], pos[3])
                if obter_peca(tab,pos1) == peca and eh_posicao_livre(tab, pos2):
                    if pos2 in obter_posicoes_adjacentes(pos1):
                        return pos1, pos2
    raise ValueError('obter_movimento_manual: escolha invalida')


def conta_peca(tab, peca):  # tabuleiro x peca -> numero de pecas no tabuleiro
    """

    :param tab:
    :param peca:
    :return:
    """
    count = 0
    colunas = obter_str_colunas()
    linhas = obter_str_linhas()
    for coluna in colunas:
        for linha in linhas:
            if peca == obter_peca(tab, cria_posicao(coluna, linha)):
                count += 1
    return count


# tabuleiro = ([0, 1, 0], [1, 0, 0], [0, 0, 1])
