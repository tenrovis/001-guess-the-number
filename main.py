import random

ran = random.randint(1, 100)
while True:
    entered = int(input("Guess the number from 1 to 100:"))

    if entered == ran:
        print("Congratulations!!!!!!! " + str(ran) + " was right!")
        break
    elif entered > ran:
        print("Enter lower")
        continue
    elif entered < ran:
        print("Enter higher")
        continue
