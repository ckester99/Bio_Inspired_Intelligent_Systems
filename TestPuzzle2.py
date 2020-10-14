import GA2, time
import numpy as np

start = time.time()
alg = GA2.GA2() #alg is a GA2

#givenNums = np.genfromtxt("CCK4x4n.txt", dtype=int)           #Import puzzle.txt into array
#alg.puzzleSize = len(givenNums)                                                 #Determines puzzle size
#givenLogic = np.genfromtxt("CCK4x4l.txt", dtype=int)          #Imports logic.txt
#numOfLogic = len(givenLogic)                                                    #Detemines number of logic statements

# givenNums = np.genfromtxt("Futoshiki Puzzle\Sample Puzzles\CCK3x3n.txt", dtype=int)
# alg.puzzleSize = len(givenNums)
# givenLogic = np.genfromtxt("Futoshiki Puzzle\Sample Puzzles\CCK3x3l.txt", dtype=int)
# numOfLogic = len(givenLogic)

# givenNums = np.genfromtxt("Futoshiki Puzzle\Sample Puzzles\CCK4x4n.txt", dtype=int)
# alg.puzzleSize = len(givenNums)
# givenLogic = np.genfromtxt("Futoshiki Puzzle\Sample Puzzles\CCK4x4l.txt", dtype=int)
# numOfLogic = len(givenLogic)

givenNums = np.genfromtxt("CCK5x5n.txt", dtype=int)
alg.puzzleSize = len(givenNums)
givenLogic = np.genfromtxt("CCK5x5l.txt", dtype=int)
numOfLogic = len(givenLogic)

print('The size of the puzzle is', alg.puzzleSize)                            #Prints puzzle number
print('The given puzzle by Hereford is:')
for m in range(alg.puzzleSize):                                               #Not needed to solve, maintence use only
    print(givenNums[m])

print('The given logic by Hereford is:')                                      #Prints logic array (Hereford's [Lesser, Greater])
for m in range(numOfLogic):                                                   #Not needed to solve, maintence use only
    print(givenLogic[m])

for i in range(alg.puzzleSize):                                                 #Sets up staticNums array
    for m in range(alg.puzzleSize):
        if (givenNums[i][m] != 0):
            alg.staticNums.append([i, m, givenNums[i][m]])
print('The static number array is:\n', alg.staticNums)                        #Maintence use only to check staticNums

for i in range(numOfLogic):                                                     #Switchs Hereford's logic to Christian's logic [Greater, Lesser]
    alg.logic.append([givenLogic[i][2],givenLogic[i][3],
    givenLogic[i][0],givenLogic[i][1]])
print('The logic array is:')                                                  #Prints Christisn's logic array
for i in range(numOfLogic):
    print(alg.logic[i])

alg.mutationRate = .05
alg.popSize = 50

alg.populate(1)
"""
for n in range(10000):
	alg.populate()
	if not n%100:
		print(n)
"""
n = 0
while not (max(alg.fitness) == 10 or n >= 100000):
	alg.populate()
	if not n%100:
		print(n)
	n += 1
	if n > 800:
		alg.populate(1)
		n = 0

best = alg.population[alg.fitness.index(max(alg.fitness))]
end = time.time()
for n in best:
	print(n)

print("Runtime: " + str((end-start)-(end-start)%.001) + "s")
