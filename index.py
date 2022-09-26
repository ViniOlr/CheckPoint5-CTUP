# modo = int(input(f"(1) O jogador-usuário contra outro jogador-usuário.\n(2) O jogador-usuário contra a máquina\nDigite qual modo você deseja: "))

jogo = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

def imprimirTabuleiro(matriz):
    print(f" {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]} ")
    print("-----------")
    print(f" {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]} ")
    print("-----------")
    print(f" {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]} ")

imprimirTabuleiro(jogo)