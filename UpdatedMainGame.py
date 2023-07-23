from MemoryGame import play1
from GuessGame import play
from CurrencyRouletteGame import play2

def load_game():
     game_choice = input("Choose game: 1 for MemoryGame, 2 for GuessGame, 3 for CurrencyRoulette\n")
     if game_choice == "1":
         print("Memory Game - a sequence of numbers will appear for 1 second and you have o guess it back")
         play1()
     elif game_choice == "2":
         print ("Guess Game - guess a number and see if you choose like the computer")
         play()
     elif game_choice == "3":
         print("Currency Roulette - try to guess the value of usd to ils")
         play2()
     else:
         print("Choix invalide")
