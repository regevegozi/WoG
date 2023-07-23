from GuessGame import play
from MemoryGame import play1
from CurrencyRouletteGame import play2

# World of Games

# Instruction and Guidelines
#   1.PLease make sure to be aligned with python's naming conventions:
#       a. Function names should always be in lowercase and separated with with_
#       b. Class names should be in CamelCase
#   2. Start a new PyCharm project and name it: World of Games and write everything there.
def welcome(): #This is the message Welcome
    name = (input("What is your name?"))
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Hello you can find many cool games to play")


def load_game(): #This is the rules of games
    print('''Please choose a game to play:
    1 . Memory Game - a sequence of numbers will appear for 1 second and you have o guess it back
    2 . Guess Game - guess a number and see if you choose like the computer
    3 . Currency Roulette - try and guess the value of a random of USD in ILS''')

def get_number(): #You ask user to enter a number
    while True:
        try:
            number = int(input("What is the game who you want to play today? "))
            if number == 1:
                print("Your chose Memory game")
                play1()
            elif number == 2:
                print("Your chose Guess game")
                play()
            elif number == 3:
                print("Your chose Currency Roulette")
                play2()
            else:
                print("Invalid choice. Try again.")
            break
        except ValueError:
            print("Its not a number.Try again")

