import random
import math

class GA1:
	xbounds = [-5.12,5.12]
	ybounds = [-5.12,5.12]
	popSize = 100
	mutationRate = .1
	selectionPoint = 512
	
	population = []
	fitness = []
	uniqueVals = 65536
	bits = 16
	

	
	def populate(self, firstGen = 0):
		nextGen = []
		if firstGen:
			for i in range(self.popSize):
				nextGen.append((random.randint(0,self.uniqueVals-1),random.randint(0,self.uniqueVals-1)))
		else:
			for i in range(self.popSize):
				if i:
					parent1 = self.rouletteWheel()
					parent2 = self.rouletteWheel()
					child = [parent1[0] - (parent1[0] % self.selectionPoint), parent1[1] - (parent1[1] % self.selectionPoint)]
					child[0] = child[0] + parent2[0] % self.selectionPoint
					child[1] = child[1] + parent2[1] % self.selectionPoint
					if random.random() < self.mutationRate:
						child[0] = child[0] ^ pow(2,random.randint(0,self.bits))
					if random.random() < self.mutationRate:
						child[1] = child[1] ^ pow(2,random.randint(0,self.bits))
						
					
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
