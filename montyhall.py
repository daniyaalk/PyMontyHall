import random, pylab, numpy as np

n = int(input("Enter number of simulations to run: "))

i = 0
switchwin = 0
stickwin = 0
stickwinlist = []
switchwinlist = []

while i < n:

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Simulation number: " + str(i+1))

    winningdoor = random.randint(1,3)
    doorchosen = random.randint(1,3)

    # If doorchosen == winningdoor, stickwin will be the winning choise, otherwise switchwin
    if doorchosen == winningdoor:
        stickwin += 1
        #pylab.scatter(stickwin, i, c='r', label='Stick')
        print("Sticking to initial option is the winning choice")
    else:
        switchwin += 1
        #pylab.scatter(switchwin, i, c='g', label='Switch')
        print("Switching initial option is the winning choice")

    stickwinlist.append(stickwin)
    switchwinlist.append(switchwin)

    print("Score so far: " if (i!=n-1) else "Final Score")
    print("Times won by sticking to initial choice: " + str(stickwin))
    print("Times won by switching choice: " + str(switchwin))
    #pylab.pause(0.05)

    i+=1

pylab.title("Comparison of switch vs stick strategy for Monty Hall Problem over " + str(n) + " trials")
pylab.plot(np.arange(0,n), stickwinlist, 'b', label='Stick')
pylab.plot(np.arange(0,n), switchwinlist, 'g', label='Switch')
pylab.legend(loc='best')
pylab.xlabel("Number of wins")
pylab.ylabel("Number of trials")
pylab.show()
