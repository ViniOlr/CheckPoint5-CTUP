def inicializarTabuleiro():
    jogo = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

    return jogo

def imprimirMenuPrincipal():
    modo = int(input(f"(1) O jogador-usuário contra outro jogador-usuário.\n(2) O jogador-usuário contra a máquina\nDigite qual modo você deseja: "))
    repeat = True
    while repeat:
        if modo == 1:
            print("modo 1")
            repeat = False
        elif modo == 2:
            print(f"Perdão o modo jogador-usuário contra a máquina ainda não está disponível!\nVocê está sendo redicionado para o modo jogador-usuário contra outro jogador-usuário!")
            repeat = False
        else:
            print("Opção inválida!")
            modo = int(input(f"(1) O jogador-usuário contra outro jogador-usuário.\n(2) O jogador-usuário contra a máquina\nDigite qual modo você deseja: "))
    listaJogador = []
    jogador1 = ""
    jogador2 = ""
    menuPrincipal = input('Jogador 1, digite (X) Para ser "X" ou (O) Para ser "O": ')
    if menuPrincipal == 'X':
        jogador1 = 'X'
        jogador2 = 'O'
        listaJogador.append(jogador1)
        listaJogador.append(jogador2)
    elif menuPrincipal == 'O':
        jogador1 = 'O'
        jogador2 = 'X'
        listaJogador.append(jogador1)
        listaJogador.append(jogador2)
    return listaJogador
    
def imprimirTabuleiro(matriz):
    print(f" {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} ")
    print("-----------")
    print(f" {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} ")
    print("-----------")
    print(f" {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} ")

def leiaCoordenadaLinha():
    linha = int(input("Digite a linha que deseja: "))
    return linha

def leiaCoordenadaColuna():
    coluna = int(input("Digite a coluna que deseja: "))
    return coluna

def posicaoValida(linha, coluna, matriz, simbolo):
    if matriz[linha-1][coluna-1] == ' ':
        matriz[linha-1][coluna-1] = simbolo
    else:
        print("Campo já preenchido")
    imprimirTabuleiro(matriz)

def imprimePontuacao(stt):
    print(f"Status do jogo: X = {stt[0]} vs O = {stt[1]}")

def verificaVencedor(matriz, simbolo, stt):
    if (matriz[0][0] == simbolo and matriz[0][1] == simbolo and matriz[0][2] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[1][0] == simbolo and matriz[1][1] == simbolo and matriz[1][2] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[2][0] == simbolo and matriz[2][1] == simbolo and matriz[2][2] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][0] == simbolo and matriz[1][0] == simbolo and matriz[2][0] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][1] == simbolo and matriz[1][1] == simbolo and matriz[2][1] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][2] == simbolo and matriz[1][2] == simbolo and matriz[2][2] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][0] == simbolo and matriz[1][1] == simbolo and matriz[2][2] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][2] == simbolo and matriz[1][1] == simbolo and matriz[2][0] == simbolo):
        print(f'O Jogador {simbolo} ganhou.')
        if simbolo == 'X':
            stt[0] += 1
        elif simbolo == 'O':
            stt[1] += 1
        imprimePontuacao(stt)
        return False
    elif (matriz[0][0] != ' ' and matriz[0][1] != ' ' and matriz[0][2] != ' ' and matriz[1][0] != ' ' and matriz[1][1] != ' ' and matriz[1][2] != ' ' and matriz[2][0] != ' ' and matriz[2][1] != ' ' and matriz[2][2] != ' '):
        print("Deu velha")
        return False
    else:
        return True



def jogar():
    modo = imprimirMenuPrincipal()
    jogador1 = modo[0]
    jogador2 = modo[1]
    stt = [0, 0]
    jogo = inicializarTabuleiro()
    imprimirTabuleiro(jogo)
    i = 1
    while verificaVencedor(jogo, jogador1, stt):
        if (i%2 == 1):
            simbolo = jogador1
        elif (i%2 == 0):
            simbolo = jogador2
        posicaoValida(leiaCoordenadaLinha(), leiaCoordenadaColuna(), jogo, simbolo)
        i += 1

jogar()