import GA2, time

"""
3 0 0 0 0
  
0 0<0 0 0
    ^   
0 0 0 0 0
. ^
0 2 0 0 0

0<4 0 0<0



(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
"""
start = time.time()
alg = GA2.GA2() #alg is a GA2
alg.staticNums = [[0,5,4],[1,1,4],[1,2,2],[3,0,5]] #this specific GA2's staticNums are these
alg.logic = [[0,3,0,2],[0,4,1,4],[1,3,1,2],[1,5,2,5],[2,2,1,2],[2,3,2,4],[3,0,2,0],[3,2,2,2],[3,3,2,3],[3,4,3,3],[4,1,4,0],[4,3,5,3],[4,5,3,5],[5,4,5,5]]
alg.puzzleSize = 6
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
	if n > 1000:
		alg.populate(1)
		n = 0

best = alg.population[alg.fitness.index(max(alg.fitness))]
end = time.time()
for n in best:
	print(n)
	
print("Runtime: " + str((end-start)-(end-start)%.001) + "s")
