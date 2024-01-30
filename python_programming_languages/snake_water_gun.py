# 1.snake, 2.water, 3.gun
# created by Chinmay Jain
import random

print("Welcome to the game!")
print("SNAKE,WATER,GUN")
user_name = str(input("Enter your name: "))
convert_user_name = user_name.upper()
def game(): 
    i=0
    ask_user = int(input("How many chances you want to play?\n"))
    while (i<(ask_user)):
        number_game = random.randint(1,3)
        user_choice = str(input("Enter your chocie: "))
        convert_user_choice = user_choice.lower()

        if number_game == 1:
            if "g" in convert_user_choice:
                print("You win")
            elif "w" in convert_user_choice:
                print("You loose")
            else:
                print("Tie")
        
        elif number_game == 2:
            if "g" in convert_user_choice:
                print("You loose")
            elif "w" in convert_user_choice:
                print("Tie")
            else:
                print("You win")

        elif number_game == 3:
            if "g" in convert_user_choice:
                print("Tie")
            elif "w"  in convert_user_choice:
                print("You win")
            else:
                print('You loose')
        i+=1

def function_continue():
    user_choice = str(input(f"Do you want to continue {convert_user_name}?\n"))
    convert_user_choice = user_choice.lower()
    if 'y' in convert_user_choice:
        game()
    elif 'n' in convert_user_choice:
        exit(0)
    else: 
        print("Please enter valid input!")
        function_continue()

while True:
    game()
    function_continue()
