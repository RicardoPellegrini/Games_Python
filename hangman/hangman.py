import pygame
import math
import random

pygame.init()

# Configurando tela
width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman Game")

# Carregando imagens
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# cores
white = (255, 255, 255)
black = (0, 0, 0)

# Variáveis do jogo
hangman_status = 0
words = ['COMPUTADOR', 'CIENCIA', 'PYTHON', 'DEVELOPER']
word = random.choice(words)
guessed = []

# Variáveis dos botões
radius = 20
gap = 15
letters = []
start_x = round((width - (radius*2 + gap) * 13)/2)
start_y = 400
A = 65          # numero 65 representa a letra A, 66 B, 67 C,...
for i in range(26):
    x = start_x + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = start_y + ((i // 13)*(gap + radius * 2))
    letters.append([x, y, chr(A + i), True])

# Fontes de texto
letter_font = pygame.font.SysFont('comicsans', 30)
word_font = pygame.font.SysFont('comicsans', 55)
title_font = pygame.font.SysFont('comicsans', 70)

# Configurando loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    window.fill(white)

    # draw title
    text = title_font.render("HANGMAN GAME!", 1, black)
    window.blit(text, (width/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter == " ":
            display_word += "  "
        elif letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, black)
    window.blit(text, (350, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(window, black, (x, y), radius, 3)  # tela, cor, posicao (centro), raio, linha
            text = letter_font.render(ltr, 1, black)
            window.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    window.blit(images[hangman_status], (100, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    window.fill(white)
    text = word_font.render(message, 1, black)
    window.blit(text, (width/2 - text.get_width() / 2, height/2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos_x, m_pos_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_pos_x)**2 + (y - m_pos_y)**2)
                    if dis <= radius:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("YOU WON!")
        break

    if hangman_status == 6:
        display_message("YOU LOST!")
        break

pygame.quit()



