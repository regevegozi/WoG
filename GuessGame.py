import random

def play():
    def get_level(): #You ask the user to enter the level of difficulty
        while True:
            try:
                level = int(input("Choose a level of difficulty (1, 2, 3, 4 or 5): "))
                if level in [1, 2, 3, 4, 5]:
                    print(f"You chose level {level}.")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("It's not a number. Try again.")

        return (level)

    difficulty = get_level()
    def generate_number(): #Generate a random number
              secret_number = random.randint(0, difficulty)
              return (secret_number)

    def get_guess_from_user():
              guess = int(input(f"Guess a number between 1 and {difficulty}: "))
              return guess

    def compare_results():
             secret_number = generate_number()
             while True:
                 guess = get_guess_from_user()
                 if guess == secret_number:
                     print("Congratulation,you guess the good number.")
                     return True
                 else:
                     print("Sorry try again.")
                     return False
    return compare_results()
