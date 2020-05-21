import random

# Lista com possíveis palavras para o jogo
palavra = ['AMARELO', 'AMOR', 'AVE', 'CANECA', 'CELULAR', 'CLUBE',
           'COPO', 'DOCE', 'ELEFANTE', 'ESCOLA', 'FOTO', 'GARFO',
           'GELEIA', 'GIRAFA', 'JANELA', 'LIMONADA', 'PAI', 'PARQUE', 'PASSARINHO']

# Garantindo que todas as palavras da lista estejam em maiúsculas
palavra = [palavra.upper() for palavra in palavra]

while True:
    # Criando um lista com uma palavra escolhida randomicamente
    esc = random.choice(palavra)
    x = list(esc)

    # Demonstrando o tamanho da palavra a ser descoberta
    forca = [' ' if letra == ' ' else '_' for letra in x]

    # Variáveis para número de vidas e para letras já escolhidas
    vidas = 6
    letras_escolhidas = []

    # Corpo do jogo
    print('-'*30)
    print('OLÁ, SEJA BEM-VINDO AO JOGO DA FORCA!')
    print('-'*30)
    for letra in forca:
        print(letra, end=' ')
    print('\n')

    while forca != x or vidas > 0:
        print('Letras já escolhidas: {}'.format(letras_escolhidas))
        y = input('Digite uma letra: ').upper()[0]
        while True:
            if y in letras_escolhidas:
                y = input('Essa letra já foi escolhida, digite outra: ').upper()[0]
            else:
                letras_escolhidas.append(y)
                break
        for ind, value in enumerate(x):
            if y == value:
                forca[ind] = value
        if y not in x:
            vidas -= 1
            print('Essa letra não consta na palavra')
            print(f'Vidas restantes: {vidas}')
        for l in forca:
            print(l, end = ' ')
        print('\n')
        if forca != x and vidas == 0:
            print('Você perdeu, amigo!')
            print(f'A palavra correta era: {esc}')
            break
        if forca == x and vidas > 0:
            print(f'Parabéns! Você venceu com {len(letras_escolhidas)} tentativas e ainda lhe restaram {vidas} vida(s)!')
            break
    jogar = input('Gostaria de jogar novamente? [S/N] ').upper()[0]
    if jogar == 'N':
        break
    if jogar != 'S' and jogar != 'N':
        jogar = input('Gostaria de jogar novamente? Escolha entre [S/N] ').upper()[0]

