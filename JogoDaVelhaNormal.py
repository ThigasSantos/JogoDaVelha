# Retorna X ou O
def jogador(tabuleiro):
    count_x = sum(row.count('X') for row in tabuleiro)
    count_o = sum(row.count('O') for row in tabuleiro)
    if count_x > count_o:
        return 'O'
    else:
        return 'X'

# Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    acoes_possiveis = []
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == ' ':
                acoes_possiveis.append((i, j))
    return acoes_possiveis

# Retorna o tabuleiro que resulta ao fazer uma jogada do vetor de ações
def resultado(tabuleiro, acao):
    novo_tabuleiro = [list(row) for row in tabuleiro]
    i, j = acao
    novo_tabuleiro[i][j] = jogador(tabuleiro)
    return novo_tabuleiro

# Retorna o ganhador, se houver
def ganhador(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]
    return ' '

# Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def final(tabuleiro):
    return ganhador(tabuleiro) != ' ' or all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

# Retorna 1 se X ganhou, -1 se O ganhou, 0 caso contrário
def custo(tabuleiro):
    ganhador_atual = ganhador(tabuleiro)
    if ganhador_atual == 'X':
        return 1
    elif ganhador_atual == 'O':
        return -1
    else:
        return 0

# Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro):
    jogador_atual = jogador(tabuleiro)
    if jogador_atual == 'X':
        melhor_custo = float('-inf')
        melhor_acao = None
        for acao in acoes(tabuleiro):
            novo_tabuleiro = resultado(tabuleiro, acao)
            custo_atual = minValor(novo_tabuleiro)
            if custo_atual > melhor_custo:
                melhor_custo = custo_atual
                melhor_acao = acao
        return melhor_acao
    else:
        melhor_custo = float('inf')
        melhor_acao = None
        for acao in acoes(tabuleiro):
            novo_tabuleiro = resultado(tabuleiro, acao)
            custo_atual = maxValor(novo_tabuleiro)
            if custo_atual < melhor_custo:
                melhor_custo = custo_atual
                melhor_acao = acao
        return melhor_acao

def maxValor(tabuleiro):
    if final(tabuleiro):
        return custo(tabuleiro)
    melhor_custo = float('-inf')
    for acao in acoes(tabuleiro):
        novo_tabuleiro = resultado(tabuleiro, acao)
        custo_atual = minValor(novo_tabuleiro)
        melhor_custo = max(melhor_custo, custo_atual)
    return melhor_custo

def minValor(tabuleiro):
    if final(tabuleiro):
        return custo(tabuleiro)
    pior_custo = float('inf')
    for acao in acoes(tabuleiro):
        novo_tabuleiro = resultado(tabuleiro, acao)
        custo_atual = maxValor(novo_tabuleiro)
        pior_custo = min(pior_custo, custo_atual)
    return pior_custo

def menu():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    while not final(tabuleiro):
        print("Estado atual:")
        for linha in tabuleiro:
            print(linha)
        print()
        if jogador(tabuleiro) == 'X':
            entrada = input("Digite a linha e a coluna da sua jogada (formato: linha,coluna): ")
            i, j = map(int, entrada.split(','))
            if 1 <= i <= 3 and 1 <= j <= 3 and tabuleiro[i-1][j-1] == ' ':
                tabuleiro[i-1][j-1] = 'X'
            else:
                print("Jogada inválida. Tente novamente.")
        else:
            print("Vez do computador:")
            melhor_acao = minimax(tabuleiro)
            tabuleiro = resultado(tabuleiro, melhor_acao)
    print("Estado final:")
    for linha in tabuleiro:
        print(linha)
    print()
    ganhador_atual = ganhador(tabuleiro)
    if ganhador_atual == ' ':
        print("O jogo terminou empatado.")
    else:
        print("O ganhador foi:", ganhador_atual)

menu()


