# TAD posicao-------------------------------------------------------------------

# Auxiliares
def obter_str_colunas():  # {} -> tuplo com strings das colunas
    """
    Fornece um tuplo com as strings dos indices das colunas.
    :return: ('a', 'b', 'c')
    """
    return 'a', 'b', 'c'


def obter_str_linhas():  # {} -> tuplo com strings das colunas
    """
    Fornece um tuplo com as strings dos indices das linhas.
    :return: ('1', '2', '3')
    """
    return '1', '2', '3'


def posicoes():  # {} -> tuplo com str de posicoes
    """
    Devolve todas as posicoes de um tabuleiro
    :return: tuplo com posicoes
    """
    str_pos = ()
    for coluna in obter_str_colunas():
        for linha in obter_str_linhas():
            str_pos += (coluna + linha,)
    return str_pos

# Construtores
def cria_posicao(col, ln):  # str x str -> posicao
    """
    Recebe duas cadeias de carateres correspondentes a coluna c
    e a linha l de uma posicao e devolve a posicao correspondente, se ambos os
    argumentos forem validos.
    :param col: Coluna, pode ser 'a', 'b' ou 'c'
    :param ln: Linha, pode ser '1', '2' ou '3'
    :return: Posicao do tabuleiro.
    """
    if col == 'a':
        col = 0
    elif col == 'b':
        col = 1
    elif col == 'c':
        col = 2
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

    return col, ln


def cria_copia_posicao(pos):  # posicao -> posicao
    """
    Permite criar uma copia de uma posicao.
    :param pos: posicao
    :return: posicao
    """
    if not eh_posicao(pos):
        raise ValueError('cria posicao: argumentos invalidos')
    copia_pos = cria_posicao(pos[0], pos[1])
    return copia_pos


# Seletores
def obter_pos_c(pos):  # posicao -> str
    """
    Permite obter a coluna de uma posicao.
    :param pos: posicao
    :return: coluna da posicao
    """
    if pos[0] == 0:
        return 'a'
    elif pos[0] == 1:
        return 'b'
    elif pos[0] == 2:
        return 'c'
    else:
        raise ValueError('obter_pos_c: argumento invalido')


def obter_pos_l(pos):  # posicao -> str
    """
    Permite obter a linha de uma posicao.
    :param pos: posicao
    :return: linha da posicao
    """
    if pos[1] == 0:
        return '1'
    elif pos[1] == 1:
        return '2'
    elif pos[1] == 2:
        return '3'
    else:
        raise ValueError('obter_pos_c: argumento invalido')


# Reconhecedores
def eh_posicao(pos):  # universal -> booleano
    """
    Indica se certo argumento e uma posicao ou nao.
    :param pos: posicao
    :return: True se o argumento for uma posicao, False caso contrario
    """
    col = pos[0]
    ln = pos[1]
    if type(col) != int or type(ln) != int:
        return False
    if col != 0 and col != 1 and col != 2:
        return False
    if ln != 0 and ln != 1 and ln != 2:
        return False
    return True


# Teste
def posicoes_iguais(pos1, pos2):  # posicao x posicao -> booleano
    """
    Indica se as posicoes inseridas sao iguais.
    :param pos1: posicao
    :param pos2: posicao
    :return: True se as posicoes forem iguais, False caso contrario
    """
    if not eh_posicao(pos1) or not eh_posicao(pos2):
        return False
    if pos1 != pos2:
        return False
    return True


# Transformador
def posicao_para_str(pos):  # posicao -> str
    """
    Transforma a posicao numa string.
    :param pos: posicao
    :return: string com a posicao
    """
    return obter_pos_c(pos) + obter_pos_l(pos)


# Funcoes Auxiliares
def cl_adjacente(cl, fn):
    """
    Funcao auxiliar que fornece uma coluna ou linha adjacente, dependendo do
    funcional utilizado.
    :param cl: str (coluna ou linha)
    :param fn: funcional (pode ser x-1 ou x+1)
    :return: indice da coluna/linha modificado, dependendo do funcional, False
    se o indice nao pertence a tabela
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
    Indica as posicoes adjacentes a posicao introduzida.
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


def cria_copia_peca(peca):  # peca -> peca
    """
    Permite copiar uma peca.
    :param peca: peca
    :return: valor da peca
    """
    if not eh_peca(peca):
        return ValueError
    return peca


# Reconhecedor
def eh_peca(arg):  # universal -> booleano
    """
    Indica se determinado argumento e uma peca.
    :param arg: valor da peca
    :return: True se o argumento for uma peca, False caso contrario
    """
    if type(arg) == int:
        if arg == 1 or arg == -1 or arg == 0:
            return True
    return False


# Teste
def pecas_iguais(peca1, peca2):  # peca x peca -> booleano
    """
    Indica se duas pecas sao iguais.
    :param peca1: peca 1
    :param peca2: peca 2
    :return: True se forem iguais, False caso contrario
    """
    if peca1 == peca2:
        return True
    return False


# Transformador
def peca_para_str(peca):  # peca -> str
    """
    Apresenta a str relativa a peca introduzida.
    :param peca:
    :return:
    """
    if peca == 1:
        return '[X]'
    elif peca == -1:
        return '[0]'
    elif peca == 0:
        return '[ ]'
    else:
        raise ValueError('peca_para_str: argumento invalido')


# Funcoes de alto nivel---------------------------------------------------------
def peca_para_inteiro(peca):  # peca -> N
    """
    Converte o valor de uma peca para o valor 1, -1 ou 0 dependendo da peca.
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
def cria_tabuleiro():  # {} -> tabuleiro
    """
    Cria um tabuleiro vazio.
    :return: tabuleiro 3x3 vazio
    """
    return [0, 0, 0], [0, 0, 0], [0, 0, 0]


def cria_copia_tabuleiro(tab):  # tabuleiro -> tabuleiro
    """
    Cria uma copia do tabuleiro introduzido.
    :param tab: tabuleiro
    :return: copia do tabuleiro
    """
    if not eh_tabuleiro(tab):
        raise ValueError()
    copia = (tab[0].copy(), tab[1].copy(), tab[2].copy())
    return copia


# Seletores
def obter_peca(tab, pos):  # tabuleiro x posicao -> peca
    """
    Permite obter uma peca de uma posicao de um tabuleiro.
    :param tab: tabuleiro
    :param pos: posicao
    :return:
    """
    peca = tab[pos[1]][pos[0]]
    return peca


def obter_vetor(tab, sel):  # tabuleiro x str -> tuplo de pecas
    """
    Permite obter uma coluna ou linha inteira de um tabuleiro.
    :param tab: tabuleiro
    :param sel: str de uma coluna ou linha (por exemplo: 'a', '1', etc...)
    :return: tuplo com as pecas das posicoes correspondente a linha/tabela
    escolhida
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
    Coloca uma peca na posicao desejada, alterando destrutivamente o tabuleiro.
    :param tab: tabuleiro
    :param peca: peca
    :param pos: posicao
    :return: tabuleiro
    """
    tab[pos[1]][pos[0]] = peca
    return tab


def remove_peca(tab, pos):  # tabuleiro x posicao -> tabuleiro
    """
    Remove a peca na posicao desejada, alterando destrutivamente o tabuleiro.
    :param tab: tabuleiro
    :param pos: posicao
    :return: tabuleiro
    """
    tab[pos[1]][pos[0]] = 0
    return tab


def move_peca(tab, pos1, pos2):  # tabuleiro x posicao x posicao -> tabuleiro
    """
    Move uma peca de uma posicao para outra, alterando destrutivamente o
    tabuleiro.
    :param tab: tabuleiro
    :param pos1: posicao original
    :param pos2: posicao destino
    :return: tabuleiro
    """
    peca = tab[pos1[1]][pos1[0]]
    tab = coloca_peca(tab, peca, pos2)
    tab = remove_peca(tab, pos1)
    return tab


# Reconhecedor
def eh_tabuleiro(arg):  # universal -> booleano
    """
    Indica se o argumento introduzido e um tabuleiro.
    :param arg: argumento
    :return: True se o argumento e um tabuleiro, False caso contrario.
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
    Indica se certa posicao de um tabuleiro esta livre.
    :param tab: tabuleiro
    :param pos: posicao
    :return: True se a posicao estiver livre, False caso contrario
    """
    if tab[pos[1]][pos[0]] == 0:
        return True
    return False


# Teste
def tabuleiros_iguais(tab1, tab2):  # tabuleiro x tabuleiro -> booleano
    """
    Indica se os tabuleiros introduzidos sao iguais
    :param tab1: tabuleiro
    :param tab2: tabuleiro
    :return: True se forem iguais, False caso contrario
    """
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1 == tab2:
        return True
    return False


# Transformadores
def tabuleiro_para_str(tab):  # tabuleiro -> str
    """
    Devolve a cadeia de caracteres que representam o tabuleiro.
    :param tab: tabuleiro
    :return: string (representacao do tabuleiro)
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
    Recebe um tuplo contendo 3 tuplos que conteem 3 inteiros 0, -1 ou 1 e
    devolve o tabuleiro equivalente.
    :param tuplo: tuplo
    :return: tabuleiro
    """
    return list(tuplo[0]), list(tuplo[1]), list(tuplo[2])


# Funcoes de alto nivel---------------------------------------------------------
def obter_ganhador(tab):  # tabuleiro -> peca
    """
    Indica se no tabuleiro fornecido existe algum vencedor.
    :param tab: tabuleiro
    :return: peca do jogador ganhador, peca livre se nao houver ganhador
    """
    x = cria_peca('X')
    o = cria_peca('O')
    livre = cria_peca(' ')
    indices = obter_str_linhas() + obter_str_colunas()

    for indice in indices:
        vetor = obter_vetor(tab, indice)
        if vetor == (x, x, x):
            return x
        if vetor == (o, o, o):
            return o
    return livre


def obter_posicoes_livres(tab):  # tabuleiro -> tuplo de posicoes
    """
    Devolve as posicoes livres num tabuleiro
    :param tab: tabuleiro
    :return: tuplo com as posicoes livres
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
    Devolve as posicoes de um tabuleiro que tenham certa peca
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
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
    Recebe uma peca e um tabuleiro e um movimento/posicao introduzidos
    manualmente, dependendo na fase em que esta o programa.
    Na fase de colocacao, recebe uma string com uma posicao.
    Na fase de movimentacao, recebe uma string com duas posicoes.
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
    """
    if peca == cria_peca('X') or peca == cria_peca('O'):
        if len(obter_posicoes_jogador(tab, peca)) < 3:
            pos = str(input('Turno do jogador. Escolha uma posicao: '))
            if len(pos) == 2 and type(pos) == str:
                pos = cria_posicao(pos[0], pos[1])
                if eh_posicao_livre(tab, pos):
                    return pos,
        if len(obter_posicoes_jogador(tab, peca)) == 3:
            pos = str(input('Turno do jogador. Escolha um movimento: '))
            if len(pos) == 4 and type(pos) == str:
                pos1 = cria_posicao(pos[0], pos[1])
                pos2 = cria_posicao(pos[2], pos[3])
                if obter_peca(tab,pos1) == peca and eh_posicao_livre(tab, pos2):
                    if pos2 in obter_posicoes_adjacentes(pos1):
                        return pos1, pos2
    raise ValueError('obter_movimento_manual: escolha invalida')


def minimax(tab, jog, prof, seq_mov):
    """

    :param tab:
    :param jog:
    :param prof:
    :param seq_mov:
    :return:
    """
    int_jog = peca_para_inteiro(jog)
    if obter_ganhador(tab) == jog or prof == 0:
        return tab, seq_mov
    else:

        for pos_jogador in obter_posicoes_jogador(tab, jog):
            for pos_adjacente in obter_posicoes_adjacentes(pos):
                if eh_posicao_livre(tab, pos_adjacente):
                    copia_tab = move_peca(cria_copia_tabuleiro(tab),
                                          pos_jogador, pos_adjacente)

                    return minimax(copia_tab, -jog, prof-1, seq_mov + )

                    if melhor_sequencia == () or jog





# tabuleiro = ([0, 1, 0], [1, 0, 0], [0, 0, 1])
