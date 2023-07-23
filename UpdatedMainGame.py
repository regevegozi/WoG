from MemoryGame import play1
from GuessGame import play
from CurrencyRouletteGame import play2

def load_game():
     game_choice = input("Choose game: 1 for Memory Game, 2 for Guess Game, 3 for Currency Roulette\n")
     if game_choice == "1":
         print("Memory Game - a sequence of numbers will appear for 1 second and you have o guess it back")
         play1()
     elif game_choice == "2":
         print ("Guess Game - guess a number and see if you choose like the computer")
         play()
     elif game_choice == "3":
         print("Currency Roulette - essayez de deviner la valeur d'un montant aléatoire de USD en ILS")
         play2()
     else:
         print("Choix invalide")
