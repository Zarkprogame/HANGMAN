import random
import os

os.system('cls')

titulo = """
**   **    ***    **   **  *******   **      **    ***    **   **      *****   **  **      *******    ***    ******  **  **
**   **   ** **   ***  **  **        ***    ***   ** **   ***  **      **   *  **  **          ***   ** **   **   *  ** **
*******   *****   **** **  **  ***   ****  ****   *****   **** **      *****     **          **      *****   ******  ***
**   **  **   **  ** ****  **   **   ** **** **  **   **  ** ****      **   *    **        ***      **   **  **  *   ** **
**   **  **   **  **   **  *******   **  **  **  **   **  **   **      *****     **        *******  **   **  **   *  **  **
"""
animals = './archivos/animals.txt'
colors = './archivos/colors.txt'
animes = './archivos/animes.txt'
mangas = './archivos/mangas.txt'

print(titulo)

game = ("""
-----GAMEMODES----

    1 for animals
    2 for colors
    3 for animes
    4 for mangas or manhwas
""")

print(game)

############################   MIRAR LETRAS Y NUMEROS NO CONTEMPLADOS #########################################
while True:
    gamemode = input('Choose your Gamemode: ')

    if gamemode == '1':
        choice = animals
    elif gamemode == '2':
        choice = colors
    elif gamemode == '3':
        choice = animes
    elif gamemode == '4':
        choice = mangas
    else:
        os.system('cls')
        print(titulo)
        print(game)
        print('Only have these options')     
        continue
    break
#####################################################################################################################
###############  1. agregar pistas para animes y mangas
###############  2. ponerle oportunidades, con dibujos ASCI en GitHub
words = []
with open(choice, 'r' , encoding='utf-8') as f:
    for line in f:
        words.append(line)
word = random.choice(words)

new_word = ''
for c in word:
    new_word += c + ' '
word_list = list(new_word)
word_list.pop(-1)
word_list.pop(-1)
word_list.pop(-1)

new_word = ''.join(word_list)

secret = (len(word) - 1) * '_ '
secret_list = list(secret)
secret_list.pop(-1)
secret = ''.join(secret_list)

word = list(word)
word.pop(-1)
word = ''.join(word)

while True:
    os.system('cls')
    print(titulo)
    print('Guess the Word: ')
    print(secret)
    if secret == new_word:
        print('Ganaste, La Palabra era ', word)
        break
    user_word = input('Type a letter and press Enter: ')
    for index,char in enumerate(word_list):
        if user_word == char:
            secret_list[index] = char
            secret = ''.join(secret_list)
    print(secret)
    

