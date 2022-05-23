#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


var = pd.read_csv("C:\\Users\\USER\\Downloads\\Demand_Coverage.csv")
print(var)


# In[3]:


population_size = 0
for i in range(len(var)):
    population_size += 1
print(population_size)


# In[4]:


lst = []
for i in range(0,population_size):
    lst.append(i)
s = pd.Series(lst)
var['Node_No'] = s.values
print(var)


# In[5]:


#Function to convert numeric value to Binary String
def Dec_to_bin(key_one):
    if key_one in range(512):
        bin_key_one = f'{key_one:09b}'
        return bin_key_one
    else:
        print("You have to enter key (0 <= key <= 511)")


# In[6]:


# Creation of a list of tuples containing node_no and corresponding demand.
demand = []
demand = var['Demand'].to_list()
node_no = []
node_no = var['Node_No'].to_list()
for i in range(0,len(node_no)):
    node_no[i] = Dec_to_bin(node_no[i])
pop_data = list(zip(node_no,demand))
#print(pop_data)


# In[7]:


#Adding unutilised nodes with demand 0 inside population_data.
import random
for i in range(population_size,512):
    pop_data.append((Dec_to_bin(i),0.0))
# Finding average of total demand of all the nodes in the network in WDNs.
total_demand = 0
for i in range(0,population_size):
    total_demand += demand[i]
average_demand = total_demand/population_size
print(average_demand)


# In[91]:


# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random

# Number of individuals in each generation
POPULATION_SIZE = 50

# Valid genes
#GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
#QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Target string to be generated
TARGET = 20

class Individual(object):
	'''
	Class representing individual in population
	'''
	global pop_data
	global average_demand
	def __init__(self, chromosome):
		self.chromosome = chromosome
		self.fitness = self.cal_fitness()

	@classmethod
	def mutated_genes(self):
		'''
		create random genes for mutation
		'''
		#global GENES
		gene = random.choice(pop_data) # In this line, I have to choose a node from 512 nodes ie sensors 
		return gene

	@classmethod
	def create_gnome(self):
		'''
		create chromosome or string of genes
		'''
		#global TARGET
		gnome_len = TARGET
		return [self.mutated_genes() for _ in range(gnome_len)] # gnome_length= no of sensors after optimisation.


	def mate(self, par2):
		'''
		Perform mating and produce new offspring
		'''
		# chromosome for offspring
		child_chromosome = []
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):

			# random probability
			prob = random.random()

			# if prob is less than 0.45, insert gene
			# from parent 1
			if prob < 0.45:
				child_chromosome.append(gp1)

			# if prob is between 0.45 and 0.90, insert
			# gene from parent 2
			elif prob < 0.90:
				child_chromosome.append(gp2)

			# otherwise insert random gene(mutate),
			# for maintaining diversity
			else:
				child_chromosome.append(self.mutated_genes())

		# create new Individual(offspring) using
		# generated chromosome for offspring
		return Individual(child_chromosome)

	def cal_fitness(self):
		'''
		Calculate fitness score, it is the number of
		characters in string which differ from target
		string.
		'''
		global TARGET
		fitness = 0
		for g in self.chromosome:
			fitness = fitness + g[1]
		fitness = fitness/TARGET
		return fitness
# 	gnome = Individual.create_gnome()
# 	print(gnome)
# 	population = []
# 	population.append(Individual(gnome))
# 	print(Individual.get_fitness())

#Driver code
def main():
	global POPULATION_SIZE
	global TARGET
	global average_demand
	#current generation
	generation = 1

	found = False
	population = []
	counter = 0
	temp_pop = []
	# create initial population
	for i in range(POPULATION_SIZE):
				gnome = Individual.create_gnome()   
				population.append([gnome,Individual(gnome).fitness]) # population array containing 50 sets of population of size 20.
# 	population = sorted(population,key = lambda x:x[1],reverse = True)
# # 	print(population[0])
# 	new = []
# 	new.extend(population[:5])
# 	parent1 = random.choice(population[:25])
# 	parent2 = random.choice(population[:25])
# 	print(parent1[0])
    
    
# 	print(parent1)
    
	while not found:

		# sort the population in increasing order of fitness score
		population = sorted(population, key = lambda x:x[1],reverse = True)

		# if the individual having lowest fitness score ie.
		# 0 then we know that we have reached to the target
		# and break the loop
		if population[0][1]/ average_demand >= 1.5:
			found = True
			break

		# Otherwise generate new offsprings for new generation
		new_generation = []

		# Perform Elitism, that mean 10% of fittest population
		# goes to the next generation
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s])

		# From 50% of fittest population, Individuals
		# will mate to produce offspring
		s = int((90*POPULATION_SIZE)/100)
		for _ in range(s):
			parent1 = random.choice(population[:25])
			parent2 = random.choice(population[:25])
			p1 = parent1[0]
			p2 = parent2[0]
			child = []
			for g1 , g2 in zip(p1,p2):
				prob = random.random()
				if prob < 0.45:
					child.append(g1)
				elif prob < 0.90:
					child.append(g2)
				else:
					child.append(random.choice(pop_data))
				child_chromosome = []
				child_chromosome.append([child,Individual(child).fitness])
                    
		new_generation.extend(child_chromosome)
		generation += 1
		population = new_generation
	print(population[0])
	print(generation)
# # 		print("Generation: {}\tString: {}\tFitness: {}".\
# # 			format(generation,
# # 			"".join(population[0].chromosome),
# # 			population[0].fitness))

# # 		generation += 1

	
# # # # 	print("Generation: {}\tString: {}\tFitness: {}".\
# # # # 		format(generation,
# # # # 		"".join(population[0].chromosome),
# # # # 		population[0].fitness))

if __name__ == '__main__':
	main()


# In[ ]:




