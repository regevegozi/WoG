from currency_converter import CurrencyConverter
import random

def play2():
    def get_level():
        level = int(input("Choose a level of difficulty 1,2,3,4 or 5"))
        while True:
            print(f"You chose level {level}.")
            if level in [1, 2, 3, 4, 5]:
                break
        return level

    difficulty=get_level()
    def get_money_interval():
        c = CurrencyConverter()
        rate = c.convert(1, 'USD', 'ILS')
        usd = int(random.uniform(1, 100))
        total_value = int(rate) * usd
        low = int(total_value - (5 - difficulty))
        high = int(total_value + (5 - difficulty))
        return total_value,low,high


    usd1, low, high = get_money_interval()
    def get_guess_from_user():
         correct_guess = False
         while not correct_guess:
             guess = int(input("Guess the value of usd$ in ILS: "))
             if guess == usd1 :
                 print("You guessed the correct number!")
                 correct_guess = True
             elif guess>=low:
                 print("You entered a larger number!")
             elif guess<=high:
                 print("You entered a smaller number!")
             else:
                 print("Try again!")
                 return guess,correct_guess

    print (get_guess_from_user())