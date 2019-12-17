def Imprimi_Tabuleiro():
    print('   +--+--+--+\n'
          '   | 1| 2| 3|')
    for i in range(0, 3):
        print('+--+--+--+--+\n|', i + 1, end='')
        for j in range(0, 3):
            print('|', Tabuleiro[i][j], end='')
        print('|')
    print('+--+--+--+--+')


def Jogador_1(nome):
    Para = True
    while Para:
        Imprimi_Tabuleiro()
        print(nome, 'é a sua vez')
        col = int(input('Informe a coluna desejada (1 - 3): '))
        lin = int(input('Informe a Linha desejada (1 - 3): '))

        if Tabuleiro[lin - 1][col - 1] == ' ':
            Tabuleiro[lin - 1][col - 1] = 'X'
            Para = False


def Jogador_2(nome):
    Para = True
    while Para:
        Imprimi_Tabuleiro()
        print(nome, 'é a sua vez')
        col = int(input('Informe a coluna desejada (1 - 3): '))
        lin = int(input('Informe a Linha desejada (1 - 3): '))

        if Tabuleiro[lin - 1][col - 1] == ' ':
            Tabuleiro[lin - 1][col - 1] = 'O'
            Para = False


def Ganhou():
    Temp = Tabuleiro
    for i in range(0, 3):
        for j in range(0, 3):
            if Temp[i][j] == ' ':
                Temp[i][j] = str(i) + str(j)

    if ((Temp[0][0] == Temp[0][1] and Temp[0][0] == Temp[0][2] and Temp[0][1] == Temp[0][1]) or
            (Temp[1][0] == Temp[1][1] and Temp[1][0] == Temp[1][2] and Temp[1][1] == Temp[1][2]) or
            (Temp[2][0] == Temp[2][1] and Temp[2][0] == Temp[2][2] and Temp[2][1] == Temp[2][2]) or
            (Temp[0][0] == Temp[1][0] and Temp[0][0] == Temp[2][0] and Temp[1][0] == Temp[2][0]) or
            (Temp[0][1] == Temp[1][1] and Temp[0][1] == Temp[2][1] and Temp[1][1] == Temp[2][1]) or
            (Temp[0][2] == Temp[1][2] and Temp[0][2] == Temp[2][2] and Temp[1][2] == Temp[2][2]) or
            (Temp[0][0] == Temp[1][1] and Temp[0][0] == Temp[2][2] and Temp[1][1] == Temp[2][2]) or
            (Temp[0][2] == Temp[1][1] and Temp[0][2] == Temp[2][0] and Temp[1][1] == Temp[2][0])):
        print('\n\n\n\n\n\n\n\t\t\t\tParabéns você Ganhou!!!\n\n\n\n\n\n\n\n')
        return True

    for i in range(0, 3):
        for j in range(0, 3):
            if Temp[i][j] == str(i) + str(j):
                Temp[i][j] = ' '


jog = 1
Jogador1 = str(input('Informe o Nome do jogador 1: '))
Jogador2 = str(input('Informe o Nome do jogador 2: '))
Tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

while True:
    if jog == 1:
        Jogador_1(Jogador1)
        jog = 2
    else:
        Jogador_2(Jogador2)
        jog = 1
    if Ganhou():
        break
