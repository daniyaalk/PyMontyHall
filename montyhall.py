import random, matplotlib

n = int(input("Enter number of simulations to run: "))

i = 0
switchwin = 0
stickwin = 0

while i < n:

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Simulation number: " + str(i+1))

    winningdoor = random.randint(1,3)
    doorchosen = random.randint(1,3)

    # If doorchosen == winningdoor, stickwin will be the winning choise, otherwise switchwin
    if doorchosen == winningdoor:
        stickwin += 1
        print("Sticking to initial option is the winning choice")
    else:
        switchwin += 1
        print("Switching initial option is the winning choice")

    print("Score so far: " if (i!=n-1) else "Final Score")
    print("Times won by sticking to initial choice: " + str(stickwin))
    print("Times won by switching choice: " + str(switchwin))
    i+=1
