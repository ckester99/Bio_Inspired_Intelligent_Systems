import random
import math

class GA1:
	puzzleSize = 5
	popSize = 100
	mutationRate = .01
	
	population = []
	fitness = []

	
	def populate(self, firstGen = 0):
		nextGen = []
		if firstGen:
			for i in range(self.popSize):
				child = []
				for m in range(self.puzzleSize):
					row = []
					for n in range(self.puzzleSize):
						row.append(random.randint(1,self.puzzleSize))
					child.append(tuple(row))
				nextGen.append(tuple(child))
		else:
			for i in range(self.popSize):
				if i:
					parent1 = self.rouletteWheel()
					parent2 = self.rouletteWheel()
					child = []
					for m in range(self.puzzleSize):
						row = []
						for n in range(self.puzzleSize):
							if random.rand() < .5:
								row.append(parent1[m,n])
							else:
								row.append(parent2[m,n])
							
							if random.rand() < mutationRate:
								row[n] = random.randint(1,self.puzzleSize)
						child.append(tuple(row))
					nextGen.append(tuple(child))
					
				else:
					nextGen.append(self.population[self.fitness.index(max(self.fitness))])
		self.population = nextGen
		self.evalFitness()
	
	def evalFitness(self):
		self.fitness = []
		for animal in self.population:
			x = animal[0]/self.uniqueVals * (self.xbounds[1]-self.xbounds[0]) + self.xbounds[0]
			y = animal[1]/self.uniqueVals * (self.ybounds[1]-self.ybounds[0]) + self.ybounds[0]
			z = (pow(x,2) - 10 * math.cos(2 * math.pi * x)) + (pow(y,2) - 10 * math.cos(2 * math.pi * y)) + 20
			if not z:
				z = .0000000001
			self.fitness.append(1/z)
	
	def rouletteWheel(self):
		max = sum(self.fitness)
		choice = random.uniform(0,max)
		index = 0
		res = 0
		for i in self.fitness:
			res += i
			if res >= choice:
				return self.population[index]
			else:
				index = index+1
