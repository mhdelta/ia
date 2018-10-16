from deap import algorithms, creator, tools, base
import numpy as np
import random
SIZE = 8

def CreateRandomBoard():
	"""Crea un tablero aleatorio con 0 y 1, donde 0 es un espacio vac¡o y 1 es un caballo"""
    matrix = []
    for i in range(SIZE):
        m = []
        for j in range(SIZE):
            if random.randint(0,100) < 7:
                m.append(1)
            else:
                m.append(0)
        matrix.append(m)
    return matrix 

toolbox = base.Toolbox()

creator.create("FitnessMin", base.Fitness, weights=(1.0, -1.0))
creator.create('Individual', list, fitness=creator.FitnessMin)


def getAttacks(matrix):
	""" Obtiene el n£mero de ataques que producen los caballos es un tablero, esta medida sirve para saber que tan
	bueno es un tablero """
    attackMatrix = []
    for i in range(SIZE):
        m = []
        # print matrix[i]
        for i in range(SIZE):
            m.append(0)
        attackMatrix.append(m)
    i = 0
    j = 0
    # print '\n', matrix
    for row in matrix:
        for col in row:
            if col == 1:
                attackMatrix[i][j] = 1
                if i < 7:
                    if j < 6:
                        if attackMatrix[i + 1][j + 2] != 1:
                            attackMatrix[i + 1][j + 2] = 2
                    if j > 1:
                        if attackMatrix[i + 1][j - 2] != 1:
                            attackMatrix[i + 1][j - 2] = 2
                if i < 6:
                    if j < 7:
                        if attackMatrix[i + 2][j + 1] != 1:
                            attackMatrix[i + 2][j + 1] = 2
                    if j > 0:
                        if attackMatrix[i + 2][j - 1] != 1:
                            attackMatrix[i + 2][j - 1] = 2
                if i > 0:
                    if j < 6:
                        if attackMatrix[i - 1][j + 2] != 1:
                            attackMatrix[i - 1][j + 2] = 2
                    if j > 1:
                        if attackMatrix[i - 1][j - 2] != 1:
                            attackMatrix[i - 1][j - 2] = 2
                if i > 1:
                    if j < 7:
                        if attackMatrix[i - 2][j + 1] != 1:
                            attackMatrix[i - 2][j + 1] = 2
                    if j > 0:
                        if attackMatrix[i - 2][j - 1] != 1:
                            attackMatrix[i - 2][j - 1] = 2
            j += 1
        j = 0
        i += 1
    return attackMatrix


def getRatio(matrix, imp=False):
	"""Deprecated, da un ratio basado en la cantidad de caballos, la cantidad de ataques y el n£mero de 
	espacios en blanco, sin embargo es mejor maximizarlas y minimizarlas individualmente """
    horses = 0
    attacks = 0
    blanks = 0
    for row in matrix:
        for num in row:
            if num == 1:
                horses += 1
            if num == 2:
                attacks += 1
            if num == 0:
                blanks += 1
    if imp:
        print 'caballos: ', horses 
        print 'espacios en blanco: ', blanks 
        print 'attacks: ', attacks
        for i in range(SIZE):
            print matrix[i] 
    return attacks, blanks


def evalOneMin(individual):
	"""Evalua un tablero """
    # print individual
    attackMatrix = []
    attackMatrix = getAttacks(individual)
    ratio = getRatio(attackMatrix)    
    return ratio

toolbox.register("individual", tools.initIterate, creator.Individual, CreateRandomBoard)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalOneMin)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.0000000001)
toolbox.register("select", tools.selTournament, tournsize=6)

def ex():
    pop = toolbox.population(n=350)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 15, stats=stats, halloffame=hof)
    a = evalOneMin(hof[0])
    if a[1] < 1:
        print "\n\nBest solution\n"
        for i in range(8):
            print hof[0][i]
        print "............................."
        atk = getAttacks(hof[0])
        getRatio(atk, True)
    else:
        ex()

ex()
