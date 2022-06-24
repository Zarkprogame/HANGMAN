from operator import contains
import random
import os

os.system('cls')

title = """
**   **    ***    **   **  *******   **      **    ***    **   **      *****   **  **      *******    ***    ******  **  **
**   **   ** **   ***  **  **        ***    ***   ** **   ***  **      **   *  **  **          ***   ** **   **   *  ** **
*******   *****   **** **  **  ***   ****  ****   *****   **** **      *****     **          **      *****   ******  ***
**   **  **   **  ** ****  **   **   ** **** **  **   **  ** ****      **   *    **        ***      **   **  **  *   ** **
**   **  **   **  **   **  *******   **  **  **  **   **  **   **      *****     **        *******  **   **  **   *  **  **
"""
start = """
   ===============|==============
     ||           |         ||
     ||           |         ||
     ||                     ||
     ||                     ||
     ||                     ||
     ||==========═══========||=
     ||                     ||  ==
     ||                     ||    == 
     ||                     ||      ==                 
___________________________________________        
    o    o    o    o    o     o    o    
   /|\  /|\  /|\  /|\  /|\   /|\  /|\ 
   / \  / \  / \  / \  / \   / \  / \  
"""
won = """
   ===============|==============
     ||           |         ||              
     ||           |         ||                  
     ||   o   I WON!        ||                  
     ||  /|┘                ||                      
     ||  / \                ||                          
     ||==========═══========||=
     ||                     ||  ==
     ||                     ||    == 
     ||                     ||      ==                 
___________________________________________     
   
    claps!  claps!  claps!  claps!                           
    o    o    o    o    o     o    o    
   /|┘  /|┘  /|┘  /|┘  /|┘   /|┘  /|┘ 
   / \  / \  / \  / \  / \   / \  / \  
"""
lose = """
   ===============|==============
     ||           |         ||
     ||           |         ||         
     ||           |         ||                
     ||           |         ||
     ||           |         ||
     ||======||   |   ======||=
     ||      ||   o         ||  ==
     ||          /|\        ||    == 
     ||          / \        ||      ==    
     ||                     ||        ==
___________________________________________
    You Lost!     You Lost!    You Lost!                           
    o    o    o    o    o     o    o    
   /|┘  /|┘  /|┘  /|┘  /|┘   /|┘  /|┘ 
   / \  / \  / \  / \  / \   / \  / \  
"""

animals = './archivos/animals.txt'
colors = './archivos/colors.txt'
cities = './archivos/cities.txt'

print(title)
print(start)

game = ("""
-----GAMEMODES----

    1 for animals
    2 for colors
    3 for cities
""")

print(game)

while True:
    gamemode = input('Choose your Gamemode: ')

    if gamemode == '1':
        choice = animals
    elif gamemode == '2':
        choice = colors
    elif gamemode == '3':
        choice = cities
    else:
        os.system('cls')
        print(title)
        print(game)
        print('Only have these options')     
        continue
    break

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

counter = 10
use_char = []

while True:
    cont_temp = 0
    os.system('cls')
    print(title)
    print(start)
    print('Guess the Word: ')
    print(secret)
    print('Used characters = ', use_char)
    print('You have',counter, 'oportunities')
    if secret == new_word:
        os.system('cls')
        print(title)
        print(won)
        print('You Won!!, The Word was', word)
        break
    user_word = input('Type a letter and press Enter: ')
    for index,char in enumerate(word_list):
        if user_word == char:
            cont_temp = 1
            secret_list[index] = char
            secret = ''.join(secret_list)
    if cont_temp == 0:
        counter -= 1
        use_char.append(user_word)
    if counter < 1:
        os.system('cls')
        print(title)
        print(lose)
        print('You didnt guess the Word, The Word was',word)
        quit()

