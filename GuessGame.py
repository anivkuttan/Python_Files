import random

Guessed_number = random.choice(range(0, 101))

counter = 0


while True:
    try:
        User_input = int(input("Enter guess number :  "))
        limit = 4
        balance_limit = limit - counter
        point = balance_limit
        if counter >= limit:
            print("you are Guess limit is over")
            print(f"Correct Guess Number is {Guessed_number}")
            print(f"Your point  is 0")
            break
        else:
            if Guessed_number > User_input:
                print(f"Guess Higher value, your balance chance is {balance_limit}")
            elif Guessed_number < User_input:
                print(f"Guess Lower number, your balance chance is {balance_limit}")
            elif Guessed_number == User_input:
                print(f"You won the Game....!!!! Guess number is {Guessed_number}")
                print(f"Your point is {point}")
                break

        counter = counter + 1
    except ValueError:
        print(" Invalid input ")
