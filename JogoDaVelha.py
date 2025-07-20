# JOGO DA VELHA

def mostrar_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))

def verificar_vitoria(tab, jogador):
    #verifica as linhas
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True
        
    #verifica as colunas
    for i in range(3):
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True
        
    #verifica as diagonais
        if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
            return True
    
        if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
            return True
        
        return False

# lista de duas dimensões (x,y)
tabuleiro =[["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

jogador_atual = "X"

for rodada in range(9):
    mostrar_tabuleiro(tabuleiro)
    escolha = input(f"Jogador {jogador_atual}, escolha uma posição de (1-9):")
    posicao = int(escolha) - 1
    ''' lógica: se escolha = 9, 9-1=8. 
        Logo, 8 // 3 = 2 (linha 2) e 8 % 3 = 2 (linha 2)
        importante: A contagem começa do 0, consequentemente,
        o 9 está na posição x=2 e y=2 (2,2). 
    '''
    linha, coluna = posicao // 3, posicao % 3

    if tabuleiro[linha][coluna] in ["X", "O"]:
        print("Posição já ocupada. Tente outra.")
        continue

    tabuleiro[linha][coluna] = jogador_atual

    if verificar_vitoria(tabuleiro, jogador_atual):
       mostrar_tabuleiro(tabuleiro)
       print(f"Jogado {jogador_atual} venceu!")
       break #finaliza o loop

    #Condição para trocar o jogador atual após o loop for (linha 13)
    if jogador_atual == "O":
       jogador_atual = "X"
    else:
       jogador_atual = "O"
