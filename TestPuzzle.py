import GA2

"""
0 0 3
  ^
2 0 0
     
0 1<0



(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
"""

alg = GA2.GA2() #alg is a GA2
alg.staticNums = [[0,2,3],[2,1,1],[1,0,2]] #this specific GA2's staticNums are these
alg.logic = [[1,1,0,1],[2,2,2,1]]

alg.populate(1)
"""
for n in range(10000):
	alg.populate()
	if not n%100:
		print(n)
"""
n = 0
while not (max(alg.fitness) == 10 or n >= 10000):
	alg.populate()
	if not n%100:
		print(n)

best = alg.population[alg.fitness.index(max(alg.fitness))]
for n in best:
	print(n)