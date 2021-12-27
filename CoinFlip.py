import random

coin_side = ("HEAD", "TAIL")
head_counter = 0
tail_counter = 0


def counter():
    global head_counter
    global tail_counter
    global A
    while True:
        try:
            A = input("Do you wanna flip a coin ---> YES or NO : ").upper()
            if A == "YES":
                side = random.choice(coin_side)
                print(side)
                if side == "HEAD":
                    head_counter += 1
                    if head_counter > 1:
                        print(f"your total Head count is {head_counter} and Tail count is {tail_counter}")
                elif side == "TAIL":
                    tail_counter += 1
                    if tail_counter > 1:
                        print(f"your total Tail count is {tail_counter} and Head count is {head_counter}")
            elif A == "NO":
                print("Thank you....See you Again...")
                break
        except ValueError:
            print("Invalid input")


A = input("Press 1 to start a game press 0 to exit the game :  ")

if A == "1":
    counter()

elif A == "0":
    print("Thank you....See you Again...")

elif A != "1":
    while True:
        print("Enter the Valid key")
        A = input("Press 1 to start a game "
                  "press 0 to exit the game :  ")
        if A == "1":
            counter()
        elif A == "0":
            print("Thank you..... See you Again......")
            break




