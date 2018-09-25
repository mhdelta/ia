from deap import algorithms, creator, tools, base
import numpy as np
import random
NUMBER = input("Give me the number ")
DIG = [str(i) for i in range(1,10)]
OP = ['+', '-', '/', '*']

def CreateRandomExpr():
    while True:
        n = random.randint(3, 11)
        if n%2 == 1:
            str = ""
            for i in range(n):
                x = random.randint(0, 8)
                y = random.randint(0, 3)
                if i%2 == 0:
                    str += DIG[x]
                else:
                    str += OP[y]
            return str

toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)

def validate(ind):
    new_ind = []
    for i in range(len(ind)):
        tmp = ind[i]
        if i%2 == 1:
            if ind[i] not in OP:
                tmp = OP[random.randint(0, 3)]
        else:
            if ind[i] not in DIG:
                tmp = DIG[random.randint(0, 8)]
        new_ind.append(str(tmp))
    return new_ind

def isValid(ind):
    for i in ind[0::2]:
        if i not in DIG:
            return False
    for i in ind[1::2]:
        if i not in OP:
            return False

def evalOneMin(individual):
    str = ""
    if isValid(individual) == False:
        individual = validate(individual)
    for i in individual:
            str += i    
    return abs(eval(str) -NUMBER) + len(str) , 



toolbox.register("expr", CreateRandomExpr)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalOneMin)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def ex():
    pop = toolbox.population(n=60)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    #stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 40, stats=stats, halloffame=hof)
    if 'False' in hof[0]:
        print "Answer not found"
    else:
        print "Hall of fame: " , hof

ex()
