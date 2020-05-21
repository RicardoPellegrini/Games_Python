
# Mostra tabuleiro
def tabuleiro():
    global pos
    return f' {pos[0]} | {pos[1]} | {pos[2]} \n___________\n ' \
           f'{pos[3]} | {pos[4]} | {pos[5]} \n___________\n' \
           f' {pos[6]} | {pos[7]} | {pos[8]} \n'

# Escolhendo o simbolo entre 'X' e 'O'
def definir_simbolo():
    global simbolo
    while simbolo not in ['X', 'O']:
        simbolo = input("Escolha entre 'X' e 'O': ").upper().strip()
    return f"Seu simbolo é '{simbolo}'"

# Definindo a posição a jogar
def jogada():
    global simbolo, pos
    jog_pos = input('Digite uma posicao de 1 a 9: ')
    while True:
        if jog_pos not in [str(num) for num in range(1, 10)]:
            jog_pos = input('Deve ser inserido um numero inteiro de 1 a 9: ')
        elif pos[int(jog_pos)-1] != '-':
            jog_pos = input('Essa posicao ja foi escolhida, escolha outra: ')
        else:
            jog_pos = int(jog_pos)
            break
    pos[jog_pos-1] = simbolo
    return tabuleiro()

# Verificando vitoria
def verif_vitoria():
    global simbolo, pos, resultado
    if pos[0] == pos[1] == pos[2] == simbolo\
            or pos[3] == pos[4] == pos[5] == simbolo\
            or pos[6] == pos[7] == pos[8] == simbolo:
        resultado = 'Vitoria'
        return f"Vitoria do simbolo '{simbolo}' pela linha!"
    elif pos[0] == pos[3] == pos[6] == simbolo\
            or pos[1] == pos[4] == pos[7] == simbolo \
            or pos[2] == pos[5] == pos[8] == simbolo:
        resultado = 'Vitoria'
        return f"Vitoria do simbolo '{simbolo}' pela coluna!"
    elif pos[0] == pos[4] == pos[8] == simbolo \
            or pos[6] == pos[4] == pos[2] == simbolo:
        resultado = 'Vitoria'
        return f"Vitoria do simbolo '{simbolo}' pela diagonal!"
    else:
        if pos.count('-') == 0:
            resultado = 'Empate'
            return 'O jogo empatou!'
        else:
            pass

# Passando a vez para o outro jogador
def passar_vez():
    global simbolo
    if simbolo == 'X':
        simbolo = 'O'
    else:
        simbolo = 'X'
    return f"Agora é a vez do '{simbolo}'"

# Estrutura geral do jogo
def jogo_da_velha():
    global resultado, simbolo, pos
    while True:
        pos = ['-' for i in range(9)]
        resultado = 0
        simbolo = 0
        print('--------------------------------')
        print('SEJA BEM-VINDO AO JOGO DA VELHA!')
        print('--------------------------------')
        print(tabuleiro())
        print(definir_simbolo())
        while True:
            print(jogada())
            print(verif_vitoria())
            if resultado == 'Vitoria' or resultado == 'Empate':
                print('Fim de jogo')
                break
            print(passar_vez())
        retry = input('Você deseja jogar novamente? [S/N] ').upper().strip()[0]
        if retry not in ['S', 'N']:
            retry = input('Você deseja jogar novamente? [S/N] ').upper().strip()[0]
        if retry == 'N':
            print('JOGO FINALIZADA, ATÉ A PRÓXIMA!!')
            break

jogo_da_velha()
