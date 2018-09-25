WIDTH = 8
HEIGHT = 8
import random
from deap import algorithms, creator, base, tools

class knight(object):
    def __init__(self, x = None, y = None):
        self._x = x if x else random.randint(0, WIDTH + 1)
        self._y = y if y else random.randint(0, HEIGHT + 1)

    def __repr__(self):
        return '(%r,%r)' % (self.x, self.y)

    def __hash__(self):
        return 1000 * self.x + self._y
    
    def attacks(self):
        return [k for k in set(knight(x + self.x, y + self.y))
                for x in [-2, -1, 1, 2] if 0 <= x + self.x < WIDTH
                for y in [-2, -1, 1, 2] if 0 <= y + self.y < HEIGHT and abs(x) != abs(y)]
    @property
    def x(self):
        return self._x
def evalKnights(individual):
    attack = set(pos for k in individual for pos in k.attacks())
    return len(individual), len(attack) # *-1 min, *+1 max
def create_board(kn = random.randint(7, 15)):
    return list(set(knight() for _ in range(kn)))

creator.create("FitnessMix", base.Fitness, weights = (-1.0, 1.0)) # weights = minimo num de caballos, maximo de casillas protegidas
creator.create("Individual", list, fitness = creator.FitnessMix)
tb = base.Toolbox
tb.register('individual', tools.initIterate, creator.Individual, create_board)
pop = tb.population(n = 300)

algorithms.eaSimple(pop, tb, cxpb = 0.5, mutpb = 0.2, ngen = 100, stacks = stats, halloffame = haf )

