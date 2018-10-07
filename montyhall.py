import random, pylab, numpy as np, argparse as ap, time, os

n = int(input("Enter number of simulations to run: "))
a = int(input("Enter door count: "))

i = 0
switchwin = 0
stickwin = 0
stickwinlist = []
switchwinlist = []

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


#Argument Parser
parser = ap.ArgumentParser()
parser.add_argument("-v", action="store_true", help="Display results so far after each trial", default=False)
args, leftovers = parser.parse_known_args()

while i < n:

    if args.v: print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if args.v: print("Simulation number: " + str(i+1))

    winningdoor = random.randint(1,a)
    doorchosen = random.randint(1,a)

    # If doorchosen == winningdoor, stickwin will be the winning choise, otherwise switchwin
    if doorchosen == winningdoor:
        stickwin += 1
        pylab.scatter(i, stickwin, c='r')
        if args.v: print("Sticking to initial option is the winning choice")
    else:
        switchwin += 1
        pylab.scatter(i, switchwin, c='g')
        if args.v: print("Switching initial option is the winning choice")

    stickwinlist.append(stickwin)
    switchwinlist.append(switchwin)

    if args.v:
        print("Score so far: " if (i!=n-1) else "Final Score")
        print("Times won by sticking to initial choice: " + str(stickwin))
        print("Times won by switching choice: " + str(switchwin))
    else:
        clear()
        print(str((i*100)/n)+"%")

    i+=1

pylab.title("Comparison of switch vs stick strategy for Monty Hall Problem over " + str(n) + " trials")
pylab.plot(np.arange(0,n), stickwinlist, 'r', label='Stick')
pylab.plot(np.arange(0,n), switchwinlist, 'g', label='Switch')
pylab.legend(loc='best')
pylab.ylabel("Number of wins")
pylab.xlabel("Number of trials")
if args.v: print("=============================================")
result = ((switchwin)/n)
expectation = ((a-1)/a)
print("Simulated probability of winning by switching: " + str(result))
print("Expected probability: " + str(expectation))
print("Error: " + str((result-expectation)*100/expectation) + "%")
pylab.show()
