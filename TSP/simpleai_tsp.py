
# SimpleAI Traveling Salesman Problem
# Author: Aaron Hung
# Date: 5/05/15
# Purpose: Traveling Salesman Problem solution using SimpleAI's framework for state space search using Hill Climbing algorithm.
# 

from simpleai.search import SearchProblem, hill_climbing_random_restarts, astar
from simpleai.search.viewers import ConsoleViewer
import random
import math
class TspProblem(SearchProblem):
    def __init__(self, cities, distances):
        '''Traveling Salesman Problem Class Constructor'''
        self.numCities = cities
        self.cityDistances = distances
        self.tour = range(49)
        self.initial_state = tuple(['1'])
    def actions(self, s):
        '''Return action list with action description[0] and resulting tour[1]'''
        actions = []
        actions = set(tuple(self.tour)) - set(s)
        # print "actions ", actions
        return actions

    def result(self, s ,a):
        '''Return resulting tour from action'''
        print list(s) + list(str(a))
        return list(s).extends(str(a))   
        
    def is_goal(self, state):
        if len(state) >= 46:
            return True
        else:
            return False


    # def cost(self, state):
    #     return 1

    def value(self, s):
        '''Return the length of the tour'''
        return self.__tour_length(s)

    def __tour_length(self, s):
        '''Return length of state or total distance of tour'''
        total_dist = 0
        # for i in range (0, self.numCities - 2):
        #     current_city = s[0][i]
        #     next_city = s[0][i + 1]
        #     current_dist = self.cityDistances[current_city][next_city]
        #     total_dist += current_dist        
        # # Add in distance for returning trip to origin of tour
        # total_dist += self.cityDistances[s[0][self.numCities - 1]][s[0][0]]        
        return total_dist

    
    def heuristic(self, state):
        return 1


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
def to_adjency(m):
    dataMatrix = []
    rows = cols = range(len(m))
    for r in rows:
        data = []
        for c in cols:
            if c > r:
                dij = dist(m[r], m[c], 'euclidean')
                data.append(dij)
            else:
                data.append(0)
        dataMatrix.append(data)
    return dataMatrix

def dist(p1, p2, type = 'euclidean'):
    if type == 'euclidean':
        xd = p1[0] - p2[0]
        yd = p1[1] - p2[1]
        return int(math.sqrt( xd*xd + yd*yd))
    if type == 'manhattan':
        xd = math.fabs(p1[0] - p2[0])
        yd = math.fabs(p1[1] - p2[1])
        return int(xd + yd)


def main():
        m = []
        m = readfile('att48.tsp')
        dataMatrix = to_adjency(m)
        # sm = csr_matrix(dataMatrix)
        # t = mst(sm)
        # problem = TspProblem(1, dataMatrix)
        # result = astar_search(TspProblem, )
        # print(result)
        problem = TspProblem(48,dataMatrix)
        result = astar(problem)
        print result

        
if __name__ == '__main__':
        main()    

