import random


def simulate():
    #0 is loss, 1 = win
    cardoor = random.randint(1,3)
    # print("cardoor = {}".format(cardoor))
    originaldoor = random.randint(1,3)
    # print("originaldoor = {}".format(originaldoor))
    spoileddoor = random.choice([i for i in range(1,4) if i not in [originaldoor,cardoor]])
    # print("qpoileddoor = {}".format(spoileddoor))
    if stay == True:
        choice = originaldoor
    else:
        choice = random.choice([i for i in range(1,4) if i not in [originaldoor,spoileddoor]])
    # print("choice = {}".format(choice))
    if choice == cardoor:
        return 1
    else: return 0
        


print("""Welcome to the Monty-Hall dilemma simulator!
he problem is as follows: you stand before three doors. Behind one of them is a brand new car,
and behind the others are two goats. You pick one of the doors, but you don't get to see its contents yet. The game-master points at one of the unchosen doors and
tells you that behind that specific door is a goat. 
You can assume that he speaks the truth, and we will assume that you're more interested in the car than in the goat.
You get the opportunity to change which door you want to open. Do you stick with the original door, or do you change your vote to the mystery door?
""")


input = input("Type 'original' to stay with your original door, or type 'change' to change to the mystery door." + "\n")
while True:
    if input == 'original':
        stay = True
        break
    elif input == 'change':
        stay = False
        break
    else:
        print("that is not a valid response, try again:")
        input = input("Type 'original' to stay with your original door, or type 'change' to change to the mystery door. ")

wins = 0
losses = 0
i=0
nrTests = 100000
while i<nrTests:
    outcome = simulate()
    if outcome == 0:
        losses += 1
    elif outcome == 1:
        wins += 1
    i+=1

winperc = wins/nrTests
loseperc = losses/nrTests
print("{} simulations were performed: ".format(nrTests))
print("Winpercentage: {0}, losepercentage: {1}.".format(winperc, loseperc))
if stay == True:
    print ("You chose... poorly")
else:
    print("You chose... wisely")



