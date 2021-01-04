# Tiago Rodrigues Vieira da Silva - no. 99335

# TAD posicao-------------------------------------------------------------------

# Construtores
def cria_posicao(col, ln):  # str x str -> posicao
    """
    Recebe duas cadeias de carateres correspondentes a coluna c
    e a linha l de uma posicao e devolve a posicao correspondente, se ambos os
    argumentos forem validos.
    :param col: Coluna, pode ser 'a', 'b' ou 'c'
    :param ln: Linha, pode ser '1', '2' ou '3'
    :return: Posicao do tabuleiro, representada por um tuplo com dois elementos,
    o primeiro sendo a coluna e o segundo a linha, que sao ambos inteiros de 0 a
    2, dependendo da posicao que se quer representar.
    """
    if col == 'a':
        col = 0
    elif col == 'b':
        col = 1
    elif col == 'c':
        col = 2
    else:
        raise ValueError('cria_posicao: argumentos invalidos')
    if ln == '1':
        ln = 0
    elif ln == '2':
        ln = 1
    elif ln == '3':
        ln = 2
    else:
        raise ValueError('cria_posicao: argumentos invalidos')
    return col, ln


def cria_copia_posicao(pos):  # posicao -> posicao
    """
    Permite criar uma copia de uma posicao.
    :param pos: posicao
    :return: posicao
    """
    if not eh_posicao(pos):
        raise ValueError('cria posicao: argumentos invalidos')
    copia_pos = (pos[0], pos[1])
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
    # uma posicao e um tuplo com dois elementos em que ambos variam de 0 a 2
    if type(pos) != tuple or len(pos) != 2:
        return False
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


# Auxiliares (tem a ver com a representacao externa da posicao)
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
    for linha in obter_str_linhas():
        for coluna in obter_str_colunas():
            str_pos += (coluna, linha),
    return str_pos


# Funcoes de alto nivel---------------------------------------------------------
def obter_posicoes_adjacentes(pos):  # posicao -> tuplo de posicoes
    """
    Indica as posicoes adjacentes a posicao introduzida.
    :param pos: posicao
    :return: tuplo com as posicoes adjacentes
    """
    posis_str = posicoes()  # tuplo com as posicoes em string
    posis = () # tuplo com as posicoes(ordem:a1, b1, c1, a2, b2, c2, a3, b3, c3)
    for pos_str in posis_str:
        posis += cria_posicao(pos_str[0], pos_str[1]),
    retorno = ()
    if pos == posis[1] or pos == posis[3] or pos == posis[4]:  # pos: b1, a2, b2
        retorno += posis[0],                                   # adjacente: a1
    if pos == posis[0] or pos == posis[2] or pos == posis[4]:  # pos: a1, c1, b2
        retorno += posis[1],                                   # adjacente: b1
    if pos == posis[1] or pos == posis[4] or pos == posis[5]:  # pos:
        retorno += posis[2],                                   # adjacente: c1
    if pos == posis[0] or pos == posis[4] or pos == posis[6]:  # pos: a1, c1, b2
        retorno += posis[3],                                   # adjacente: a2
    if pos in posis and pos != posis[4]:                       # pos: todas
        retorno += posis[4],                                   # adjacente: b2
    if pos == posis[2] or pos == posis[4] or pos == posis[8]:  # pos: c1, b2, c3
        retorno += posis[5],                                   # adjacente: c2
    if pos == posis[3] or pos == posis[4] or pos == posis[7]:  # pos: a2, b2, b3
        retorno += posis[6],                                   # adjacente: a3
    if pos == posis[4] or pos == posis[6] or pos == posis[8]:  # pos: b2, a3, c3
        retorno += posis[7],                                   # adjacente: b3
    if pos == posis[4] or pos == posis[5] or pos == posis[7]:  # pos: b2, c2, b3
        retorno += posis[8],                                   # adjacente: c3
    return retorno


# TAD peca----------------------------------------------------------------------

# Construtor
def cria_peca(s):  # str -> peca
    """
    Recebe uma cadeia de carateres correspondentea uma peca e devolve a peca
    correspondente se o argumento for valido.
    :param s: string da peca (pode ser 'X', 'O' ou ' ')
    :return: peca, que e representada internamente como o set de um elemento,
    que contem um inteiro -1, 0 ou 1 dependendo se a peca e 'O', ' ' ou 'X'
    respetivamente
    """
    if s != 'X' and s != 'O' and s != ' ':
        raise ValueError('cria_peca: argumento invalido')
    if s == 'X':
        return {1}
    elif s == 'O':
        return {-1}
    elif s == ' ':
        return {0}


def cria_copia_peca(peca):  # peca -> peca
    """
    Permite copiar uma peca.
    :param peca: peca
    :return: valor da peca
    """
    if not eh_peca(peca):
        return ValueError('cria_copia_peca: argumento invalido')
    if peca == cria_peca(' '):
        return cria_peca(' ')
    if peca == cria_peca('X'):
        return cria_peca('X')
    if peca == cria_peca('O'):
        return cria_peca('O')


# Reconhecedor
def eh_peca(arg):  # universal -> booleano
    """
    Indica se determinado argumento e uma peca.
    :param arg: valor da peca
    :return: True se o argumento for uma peca, False caso contrario
    """
    if arg == cria_peca('X') or arg == cria_peca('O') or arg == cria_peca(' '):
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
    if not eh_peca(peca1) or not eh_peca(peca2):
        return False
    if peca1 == peca2:
        return True
    return False


# Transformador
def peca_para_str(peca):  # peca -> str
    """
    Apresenta a str relativa a peca introduzida.
    :param peca: peca
    :return: string com a representacao da peca
    """
    if peca == cria_peca('X'):
        return '[X]'
    if peca == cria_peca('O'):
        return '[O]'
    if peca == cria_peca(' '):
        return '[ ]'


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


def inteiro_para_peca(inteiro):  # N -> peca
    """
    Converte um inteiro 1, -1 ou 0 para a peca correspondente
    :param inteiro: inteiro com o valor de 1, -1 ou 0
    :return: peca
    """
    if inteiro == 1:
        return cria_peca('X')
    elif inteiro == -1:
        return cria_peca('O')
    elif inteiro == 0:
        return cria_peca(' ')
    else:
        return ValueError('inteiro_para_peca: argumento invalido')


# TAD tabuleiro-----------------------------------------------------------------

# Construtor
def cria_tabuleiro():  # {} -> tabuleiro
    """
    Cria um tabuleiro vazio.
    :return: tabuleiro 3x3 vazio, sendo representado por um tuplo com 3 listas,
    cada uma com 3 pecas. Uma lista representa uma linha.
    """
    return [cria_peca(' '), cria_peca(' '), cria_peca(' ')], \
           [cria_peca(' '), cria_peca(' '), cria_peca(' ')], \
           [cria_peca(' '), cria_peca(' '), cria_peca(' ')],


def cria_copia_tabuleiro(tab):  # tabuleiro -> tabuleiro
    """
    Cria uma copia do tabuleiro introduzido.
    :param tab: tabuleiro
    :return: copia do tabuleiro
    """
    if not eh_tabuleiro(tab):
        raise ValueError('cria_copia_tabuleiro: tabuleiro invalido')
    copia = (tab[0].copy(), tab[1].copy(), tab[2].copy())
    return copia


# Seletores
def obter_peca(tab, pos):  # tabuleiro x posicao -> peca
    """
    Permite obter uma peca de uma posicao de um tabuleiro.
    :param tab: tabuleiro
    :param pos: posicao
    :return: peca
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
        sel = int(sel) - 1  #
        return tuple(tab[sel])  #
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
    tab[pos[1]][pos[0]] = cria_peca(' ')
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
    if pos1 != pos2:
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
    if type(arg) != tuple or len(arg) != 3:  # tem que ser tuplo e lenght = 3
        return False
    for elmts in arg:                     # elementos do tuplo tem que ser lista
        if type(elmts) != list or len(elmts) != 3:
            return False
        for elmt in elmts:
            if elmt == cria_peca('X'):
                x_count += 1
            if elmt == cria_peca('O'):
                o_count += 1
    if x_count > 3 or o_count > 3:      # so pode ter no maximo 3 pecas no tab
        return False  # e nao ter mais uma peca que outra
    if x_count > o_count + 1 or o_count > x_count + 1:
        return False
    if obter_ganhador(arg) != cria_peca(' '):     # verificar se ha 2 ganhadores
        pos = obter_posicoes_jogador(arg, obter_ganhador(arg))[0]
        peca = obter_peca(arg, pos)
        remove_peca(arg, pos)
        if obter_ganhador(arg) != cria_peca(' '):
            coloca_peca(arg, peca, pos)
            return False
        coloca_peca(arg, peca, pos)
    return True


def eh_posicao_livre(tab, pos):  # tabuleiro x posicao -> booleano
    """
    Indica se certa posicao de um tabuleiro esta livre.
    :param tab: tabuleiro
    :param pos: posicao
    :return: True se a posicao estiver livre, False caso contrario
    """
    if tab[pos[1]][pos[0]] == cria_peca(' '):
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
    tabstr = '   a   b   c\n'  # indice colunas
    for linha in range(3):
        tabstr += str(linha + 1)+' '  # indice linhas
        for coluna in range(3):
            tabstr += peca_para_str(tab[linha][coluna])  # elementos
            if coluna < 2:
                tabstr += '-'  # separadores
            else:
                if linha < 2:
                    tabstr += '\n'
        if linha == 0:
            tabstr += '   | \ | / |\n'
        if linha == 1:
            tabstr += '   | / | \ |\n'
    return tabstr


def tuplo_para_tabuleiro(tuplo):  # tuplo -> tabuleiro
    """
    Recebe um tuplo contendo 3 tuplos que conteem 3 inteiros 0, -1 ou 1 e
    devolve o tabuleiro equivalente.
    :param tuplo: tuplo
    :return: tabuleiro
    """
    tab = ()
    for elemts in tuplo:
        linha = []
        for elemt in elemts:
            if elemt == 0:
                linha += cria_peca(' '),
            if elemt == 1:
                linha += cria_peca('X'),
            if elemt == -1:
                linha += cria_peca('O'),
        tab += linha.copy(),
    return tab


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
    posis = ()
    for linha in linhas:
        for coluna in colunas:
            if pecas_iguais(obter_peca(tab, cria_posicao(coluna, linha)),
                            cria_peca(' ')):
                posis += (cria_posicao(coluna, linha),)
    return posis


def obter_posicoes_jogador(tab, peca):  # tabuleiro x peca -> tuplo de posicoes
    """
    Devolve as posicoes de um tabuleiro que tenham certa peca
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
    """
    colunas = obter_str_colunas()
    linhas = obter_str_linhas()
    posis = ()
    for linha in linhas:
        for coluna in colunas:
            if pecas_iguais(obter_peca(tab, cria_posicao(coluna, linha)), peca):
                posis += (cria_posicao(coluna, linha),)
    return posis


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
    linhas = obter_str_linhas()
    colunas = obter_str_colunas()
    if len(obter_posicoes_jogador(tab, peca)) < 3:  # fase de colocacao
        pos = str(input('Turno do jogador. Escolha uma posicao: '))
        if len(pos) == 2 and pos[0] in colunas and pos[1] in linhas:
            pos = cria_posicao(pos[0], pos[1])
            if eh_posicao_livre(tab, pos):
                return pos,
    if len(obter_posicoes_jogador(tab, peca)) == 3:  # fase de movimentacao
        pos = str(input('Turno do jogador. Escolha um movimento: '))
        if len(pos) == 4 and pos[0] in colunas and pos[1] in linhas \
                and pos[2] in colunas and pos[3] in linhas:
            pos1 = cria_posicao(pos[0], pos[1])
            pos2 = cria_posicao(pos[2], pos[3])
            if obter_peca(tab, pos1) == peca:
                if eh_posicao_livre(tab, pos2):
                    if pos2 in obter_posicoes_adjacentes(pos1):
                        return pos1, pos2
                if posicoes_iguais(pos1, pos2) and \
                        len(obter_pos_adj_livres(tab, pos1)) == 0:
                    return pos1, pos2
    raise ValueError('obter_movimento_manual: escolha invalida')


def obter_pos_adj_livres(tab, pos):  # tabuleiro x posicao -> tuplo com posicoes
    """
    Recebe uma posicao e um tabuleiro e indica quais sao as posicoes adjacentes
    a essa posicao que estao livres
    :param tab: tabuleiro
    :param pos: posicao
    :return: tuplo com posicoes adjacentes livres
    """
    posis = ()
    for pos_adjacente in obter_posicoes_adjacentes(pos):
        if eh_posicao_livre(tab, pos_adjacente):
            posis += pos_adjacente,
    return posis


def minimax(tab, jog, prof, seq_mov):
    # tabuleiro x inteiro x inteiro x tuplo -> tuplo
    """
    Funcao que implementa o algoritmo minimax fornecido no enunciado do projeto.
    :param tab: tabuleiro
    :param jog: valor do jogador (1 para X, -1 para O)
    :param prof: profundidade da recursao desejada
    :param seq_mov: sequencia de movimentos, inicializa-se com um tuplo vazio
    :return: tuplo contendo no primeiro elemento o valor do jogador e no
    segundo um tuplo contendo movimentos (tuplo com a posicao de origem e de
    destino)
    """
    if peca_para_inteiro(obter_ganhador(tab)) == jog or prof == 0:
        return peca_para_inteiro(obter_ganhador(tab)), seq_mov
    else:
        melhor_res = -jog
        melhor_seq_mov = ()
        for pos_jogador in obter_posicoes_jogador(tab, inteiro_para_peca(jog)):
            for pos_adjacente in obter_posicoes_adjacentes(pos_jogador):
                if eh_posicao_livre(tab, pos_adjacente):
                    t = move_peca(cria_copia_tabuleiro(tab), pos_jogador,
                                  pos_adjacente)
                    if eh_tabuleiro(t):
                        novo_res, nova_seq_mov = \
                            minimax(t, -jog, prof - 1, seq_mov +
                                    ((pos_jogador,) + (pos_adjacente,),))
                        if melhor_seq_mov == () or \
                                (novo_res > melhor_res and jog == 1) or \
                                (novo_res < melhor_res and jog == -1):
                            melhor_res, melhor_seq_mov = novo_res, nova_seq_mov
        return melhor_res, melhor_seq_mov


def vitoria(tab, peca):  # tab x peca -> posicao
    """
    Deteta uma posicao onde possa haver uma possivel vitoria, retornando essa
    mesma posicao. Caso contrario devolve 0
    :param tab: tabuleiro
    :param peca: peca
    :return: posicao ou 0
    """
    for coluna in obter_str_colunas():
        for linha in obter_str_linhas():
            pos = cria_posicao(coluna, linha)
            if eh_posicao_livre(tab, pos):
                copia_tab = coloca_peca(cria_copia_tabuleiro(tab), peca, pos)
                if obter_ganhador(copia_tab) != cria_peca(' '):
                    return pos,
    return 0


def bloqueio(tab, peca):  # tab x peca -> posicao
    """
    Deteta uma posicao onde possa haver uma possivel vitoria adversaria,
    retornando essa mesma posicao. Devolve 0 caso contrario.
    :param tab: tabuleiro
    :param peca: peca
    :return: posicao ou 0
    """
    jog = peca_para_inteiro(peca)
    peca_contraria = inteiro_para_peca(-jog)
    return vitoria(tab, peca_contraria)


def centro(tab):  # tab -> posicao
    """
    Devolve a posicao do centro se estiver livre, 0 caso contrario
    :param tab: tabuleiro
    :return: posicao ou 0
    """
    if eh_posicao_livre(tab, cria_posicao('b', '2')):
        return cria_posicao('b', '2'),
    return 0


def canto_vazio(tab):  # tab -> posicao
    """
    Devolve a posicao do primeiro canto que estiver livre. Se nao estiver livre
    nenhum canto devolve o inteiro 0
    :param tab: tabuleiro
    :return: posicao ou 0
    """
    cantos = (cria_posicao('a', '1'),
              cria_posicao('c', '1'),
              cria_posicao('a', '3'),
              cria_posicao('c', '3'),)
    for canto in cantos:
        if eh_posicao_livre(tab, canto):
            return canto,
    return 0


def lateral_vazia(tab):  # tab -> posicao
    """
    Devolve a posicao da primeira lateral que estiver livre. Se nao estiver
    livre nenhuma lateral devolve o inteiro 0.
    :param tab: tabuleiro
    :return: posicao ou 0
    """
    laterais = (cria_posicao('b', '1'),
                cria_posicao('a', '2'),
                cria_posicao('c', '2'),
                cria_posicao('b', '3'),)
    for lateral in laterais:
        if eh_posicao_livre(tab, lateral):
            return lateral,
    return 0


def fase_colocacao(tab, peca):  # tabuleiro x peca -> posicao
    """
    Funcao auxiliar da "obter_movimento_auto" para a fase de colocacao.
    :param tab: tabuleiro
    :param peca: peca
    :return: posicao
    """
    if vitoria(tab, peca) != 0:
        return vitoria(tab, peca)
    if bloqueio(tab, peca) != 0:
        return bloqueio(tab, peca)
    if centro(tab) != 0:
        return centro(tab)
    if canto_vazio(tab) != 0:
        return canto_vazio(tab)
    if lateral_vazia(tab) != 0:
        return lateral_vazia(tab)
    return 0


def facil(tab, peca):  # tab x peca -> tuplo com posicoes
    """
    Permite obter o movimento no tabuleiro de acordo com a dificuldade desejada
    (facil)
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
    """
    for pos_peca in obter_posicoes_jogador(tab, peca):
        for pos_adjacente in obter_posicoes_adjacentes(pos_peca):
            if eh_posicao_livre(tab, pos_adjacente):
                return pos_peca, pos_adjacente


def normal(tab, peca):  # tab x peca -> tuplo com posicoes
    """
    Permite obter o movimento no tabuleiro de acordo com a dificuldade desejada
    (normal)
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
    """
    movimentos = minimax(tab, peca_para_inteiro(peca), 1, ())
    return movimentos[1][0]


def dificil(tab, peca):  # tab x peca -> tuplo com posicoes
    """
    Permite obter o movimento no tabuleiro de acordo com a dificuldade desejada
    (dificil)
    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo com posicoes
    """
    movimentos = minimax(tab, peca_para_inteiro(peca), 5, ())
    return movimentos[1][0]


def obter_movimento_auto(tab, peca, dif):
    # tab x peca x str -> tuplo com posicoes
    """
    Funcao que fornece automaticamente um movimento de acordo com a dificuldade
    desejada.
    :param tab: tabuleiro
    :param peca: peca
    :param dif: string ( 'facil', 'normal' ou 'dificil')
    :return: tuplo com posicoes
    """
    if len(obter_posicoes_jogador(tab, peca)) < 3:
        return fase_colocacao(tab, peca)
    elif len(obter_posicoes_jogador(tab, peca)) == 3:
        if dif == 'facil':
            return facil(tab, peca)
        elif dif == 'normal':
            return normal(tab, peca)
        elif dif == 'dificil':
            return dificil(tab, peca)
        else:
            raise ValueError('obter_movimento_auto:')
    else:
        return ValueError('obter_movimento_auto:')


def eh_dificuldade(dificuldade):  # str -> booleano
    """
    Funcao que verifica se o argumento introduzido e uma dificuldade valida
    :param dificuldade: "facil", "normal", "dificil"
    :return: True ou False
    """
    if dificuldade == 'facil' or \
       dificuldade == 'normal' or \
       dificuldade == 'dificil':
        return True
    return False


def moinho(peca_str, dificuldade):  # str x str -> str
    """
    :param peca_str: string que representa uma peca ("[X]" ou "[O]")
    :param dificuldade: string que representa uma dificuldade ("facil", "normal"
    ou "dificil")
    :return: string que representa a peca do vencedor ("[X]" ou "[O]")
    """
    if not eh_dificuldade(dificuldade):
        raise ValueError('moinho: argumentos invalidos')
    if peca_str == peca_para_str(cria_peca('X')):
        jog = peca_para_inteiro(cria_peca('X'))
    elif peca_str == peca_para_str(cria_peca('O')):
        jog = peca_para_inteiro(cria_peca('O'))
    else:
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade '+dificuldade+'.')
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    if jog == peca_para_inteiro(cria_peca('O')):
        print('Turno do computador ('+dificuldade+'):')
        mov = obter_movimento_auto(tab, inteiro_para_peca(-jog), dificuldade)
        coloca_peca(tab, inteiro_para_peca(-jog), mov[0])
        print(tabuleiro_para_str(tab))
    return auxiliar_moinho(tab, jog, dificuldade)


def auxiliar_moinho(tab, jog, dificuldade):
    """
    Funcao auxiliar da funcao "moinho".
    :param tab: tabuleiro
    :param jog: representacao inteira de uma peca (-1 ou 1)
    :param dificuldade: str da dificuldade
    :return: str da peca do vencedor
    """
    while obter_ganhador(tab) == cria_peca(' '):
        mov = obter_movimento_manual(tab, inteiro_para_peca(jog))
        if len(mov) == 1:
            coloca_peca(tab, inteiro_para_peca(jog), mov[0])
        else:
            move_peca(tab, mov[0], mov[1])
        print(tabuleiro_para_str(tab))
        if obter_ganhador(tab) != cria_peca(' '):
            break
        print('Turno do computador (' + dificuldade + '):')
        mov = obter_movimento_auto(tab, inteiro_para_peca(-jog), dificuldade)
        if len(mov) == 1:
            coloca_peca(tab, inteiro_para_peca(-jog), mov[0])
        else:
            move_peca(tab, mov[0], mov[1])
        print(tabuleiro_para_str(tab))
    return peca_para_str(obter_ganhador(tab))
