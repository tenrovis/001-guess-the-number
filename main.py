import random

attempt = 0
ran = random.randint(1, 100)
tex = "Total attempts "
while True:
    try:
        entered = int(input("Guess the number from 1 to 100:"))
        if entered < 1 or entered > 100:
            print("Enter number between 1 and 100")
            continue
        attempt += 1
        if entered == ran:
            print("Congratulations!!!!!!! " + str(ran) + " was right!")
            print(tex + str(attempt))
            break
        elif entered > ran:
            print("Enter lower")
        elif entered < ran:
            print("Enter higher")
    except ValueError:
        print("You can enter only number")
