import random

n = int(input("Enter number of simulations to run: "))

i = 0
switchwin = 0
stickwin = 0

while i < n:
    winningdoor = random.randint(1,3)
    doorchosen = random.randint(1,3)
    print(str(winningdoor)+"=>"+str(doorchosen) + "WIN" if (winningdoor==doorchosen) else "LOSS")
    i+=1
