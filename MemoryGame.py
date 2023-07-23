import random,time

def play1():
    def get_level():
        level = int(input("Choose a level of difficulty 1,2,3,4 or 5"))
        while True:
            print(f"You chose level {level}.")
            if level in [1, 2, 3, 4, 5]:
                break
        return level

    difficulty = get_level()
    def generate_sequence():
             random_numbers = [random.randint(1, 101) for _ in range(difficulty)]
             time.sleep(0.7)
             return random_numbers

    def get_list_from_user():
        list = [int(i) for i in input(f"Enter {difficulty} number with space ").split()]
        if len(list) != difficulty:
            print(f'It is an error: {len(list)} number. You need to enter {difficulty} number!')
        return list

    sequence=generate_sequence()
    user=get_list_from_user()
    def is_list_equal(): #A function to compare two lists
            if  user == sequence:
                # print("you guess all numbers")
                return True
            if user != sequence:
                # print("you do a mistake")
                return False
            return is_list_equal()

    print(is_list_equal())