import random
import math

class GA2:
	puzzleSize = 3 #Dimension of puzzle, nxn
	popSize = 100
	mutationRate = .01
	
	logic = [] #[m1,n1,m2,n2] representation 1>2 
	staticNums = []
	
	population = []
	fitness = []
	

	
	def populate(self, firstGen = 0): #First generation if firstGen is true
		nextGen = []
		if firstGen: #Generates random population if first generation
			for i in range(self.popSize):
				child = []
				for m in range(self.puzzleSize):
					row = []
					for n in range(self.puzzleSize):
						row.append(random.randint(1,self.puzzleSize))
					child.append(row)
				for nums in self.staticNums:
					child[nums[0]][nums[1]] = nums[2]
				nextGen.append(child)
		else: #This is the real populate function
			for i in range(self.popSize):
				if i:
					parent1 = self.rouletteWheel() #Selects two parents through roulette wheel
					parent2 = self.rouletteWheel()
					child = []
					for m in range(self.puzzleSize): #Iterates through all genes for crossover
						row = []
						for n in range(self.puzzleSize):
							if random.random() < .5: #50% crossover rate
								row.append(parent1[m][n])
							else:
								row.append(parent2[m][n])
							
							if random.random() < self.mutationRate: #if mutation occurs insert random value at gene
								row[n] = random.randint(1,self.puzzleSize)
						child.append(row)
						
					for nums in self.staticNums:
						child[nums[0]][nums[1]] = nums[2]
					nextGen.append(child)
					
				else:
					nextGen.append(self.population[self.fitness.index(max(self.fitness))])
		self.population = nextGen
		self.evalFitness()
		"""
		lastGen = self.population.copy()
		lastFit = self.fitness.copy()
		self.population = nextGen
		self.evalFitness()
		selectionPool = lastGen.extendself.population
		selectionFit = lastFit + self.fitness
		nextPop = []
		nextFit = []
		selectionFit.sort(reverse = True)
		
		for i in range(self.popSize):
			fit = selectionFit[i]
			nextFit.append(fit)
			nextPop.append(selectionPool[selectionFit.index(fit)])
		self.population = nextPop
		self.fitness = nextFit
		"""
	
		
	
	def evalFitness(self):
		self.fitness = [] #Initializes fitness array
		for animal in self.population:
			currFit = 0
			
			for i in range(self.puzzleSize): #Gives worse fitness scores to members that have repeating elements in rows or columns
				rowNums,colNums = [0]*self.puzzleSize,[0]*self.puzzleSize
				
				for element in animal[i]:
					rowNums[element-1] += 1
				for element in rowNums:
					currFit += abs(element-1)
			
				for element in [row[i] for row in animal]:
					colNums[element-1] += 1
				for element in colNums:
					currFit += abs(element-1)
					
			for i in self.logic: #Gives worse fitness score for members that fail logic requirements
				if not animal[i[0]][i[1]] > animal[i[2]][i[3]]:
					currFit += 10
			
			if not currFit:
				currFit = .1
			self.fitness.append(1/currFit)
	
	def rouletteWheel(self): #Returns a member of the population with weighted average determined by fitness array
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
