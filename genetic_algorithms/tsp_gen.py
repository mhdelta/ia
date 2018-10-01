from deap import algorithms, creator, tools, base
import numpy as np
import random
import math


def readfile(filename):
    with open(filename) as f:
        matrix = []
        line = ''
        for line in f:
                line = line.split()
                if 'NODE_COORD_SECTION' in line:
                        break
        for line in f:
                if 'EOF' not in line:
                        split = line.split()
                        matrix.append([int(split[1]), int(split[2])])
        return matrix


def dist(p1, p2, type='euclidean'):
    if type == 'euclidean':
        xd = p1[0] - p2[0]
        yd = p1[1] - p2[1]
        return int(math.sqrt(xd*xd + yd*yd))
    if type == 'manhattan':
        xd = math.fabs(p1[0] - p2[0])
        yd = math.fabs(p1[1] - p2[1])


def to_adjency(m, from_matrix=None):
    if from_matrix:
        dataMatrix = []
        rows = cols = m
        for r in rows:
            data = []
            for c in cols:
                # if c > r:
                dij = from_matrix[int(str(r))][int(str(c))]
                data.append(dij)
                # else:
                #     data.append(0)
            dataMatrix.append(data)
    else:
        dataMatrix = []
        rows = cols = range(len(m))
        for r in rows:
            data = []
            for c in cols:
                # if c > r:
                dij = dist(m[r], m[c], 'euclidean')
                data.append(dij)
                # else:
                #     data.append(0)
            dataMatrix.append(data)
    return dataMatrix


m = []
m = readfile('att48.tsp')
DATAMATRIX = to_adjency(m)
NUMBERS = range(1, 48)


def readfile(filename):
    with open(filename) as f:
        matrix = []
        line = ''
        for line in f:
                line = line.split()
                if 'NODE_COORD_SECTION' in line:
                        break
        for line in f:
                if 'EOF' not in line:
                        split = line.split()
                        matrix.append([int(split[1]), int(split[2])])
        return int(xd + yd)


def to_adjency(m, from_matrix=None):
    if from_matrix:
        dataMatrix = []
        rows = cols = m
        for r in rows:
            data = []
            for c in cols:
                # if c > r:
                dij = from_matrix[int(str(r))][int(str(c))]
                data.append(dij)
                # else:
                #     data.append(0)
            dataMatrix.append(data)
    else:
        dataMatrix = []
        rows = cols = range(len(m))
        for r in rows:
            data = []
            for c in cols:
                # if c > r:
                dij = dist(m[r], m[c], 'euclidean')
                data.append(dij)
                # else:
                #     data.append(0)
            dataMatrix.append(data)
    return dataMatrix


def CreateRandomExpr():
    lista = []
    for i in range(1, 48):
        lista.append(i)
    return random.sample(lista, len(lista)) 


toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create('Individual', list, fitness=creator.FitnessMin)


def isValid(individual):
    if len(individual) != len(set(individual)):
        return False
    else:
        return True


def validate(individual):
    final_list = []
    for num in individual:
        if num not in final_list:
            final_list.append(num)
        else:
            x = random.randint(1, 48)
            while x in final_list:
                x = random.randint(1, 48)
            final_list.append(x)
    return final_list


def evalOneMin(individual):
    ''' Debo devolver la distancia total de las ciudades'''
    total_dist = 0
    if not isValid(individual):
        individual = validate(individual)
        print individual
    for i in range(0, 46):  # 48 ciudades menos dos 
        if int(i) < 45:
            current_city = individual[i]
            next_city = individual[i + 1]
            if int(current_city) < 45 and int(next_city) < 45:
                current_dist = DATAMATRIX[int(current_city)][int(next_city)]
                total_dist += current_dist
    return total_dist,  


toolbox.register("expr", CreateRandomExpr)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", evalOneMin)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


def ex():
    pop = toolbox.population(n=500)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    #  stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 40, stats=stats, halloffame=hof)
    print('\n' * 10)
    print "Hall of fame and distance: ", evalOneMin(hof[0])


ex()
