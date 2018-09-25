
# SimpleAI Traveling Salesman Problem
# Author: Aaron Hung
# Date: 5/05/15
# Purpose: Traveling Salesman Problem solution using SimpleAI's framework for state space search using Hill Climbing algorithm.
# 

from aima.search import Problem, astar_search as astar
from scipy import sparse
import random
import math
class TspProblem(Problem):
    def __init__(self, cities, distances, initial_city):
        '''Traveling Salesman Problem Class Constructor'''
        self.numCities = cities
        self.cityDistances = distances
        self.tour = []
        for i in range(48):
            self.tour.append(str(i))
        self.initial = initial_city
    
    def actions(self, s):
        '''Return action list with action description[0] and resulting tour[1]'''
        actions = []
        actions = set(tuple(self.tour)) - set(s)
        # print "actions ", actions
        return actions

    def result(self, s ,a):
        '''Return resulting tour from action'''
        l = []
        l.append(a)
        extended = (list(s) + l)
        return tuple(extended)
        
    def goal_test(self, state):
        if len(state) >= 46:
            print self.value(state)
            return True
        else:
            return False

    # def path_cost(self,  city1, city2, c = 0, action = ['0']):
    #     """Return the cost of a solution path that arrives at state2 from
    #     state1 via action, assuming cost c to get up to state1. If the problem
    #     is such that the path doesn't matter, this function will only look at
    #     state2.  If the path does matter, it will consider c and maybe state1
    #     and action. The default method costs 1 for every step in the path."""
    #     for i in range (0, self.numCities - 2):
    #         current_dist = self.cityDistances[int(str(city1[0]))][int(str(city2[0]))]
    #     # Add in distance for returning trip to origin of tour
    #     return current_dist

    def value(self, s):
        '''Return the length of the tour'''
        return self.__tour_length(s)

    def __tour_length(self, s):
        '''Return length of state or total distance of tour'''
        total_dist = 0
        for i in range (0, self.numCities - 2):
            if int(i) < 45:
                current_city = s[i]
                next_city = s[i + 1]
                if int(current_city) < 45 and int(next_city) < 45:
                    current_dist = self.cityDistances[int(current_city)][int(next_city)]
                    total_dist += current_dist
        return total_dist

    def h(self, node):
        remaining_cities = set(tuple(self.tour)) - set(node.state)
        m = to_adjency(remaining_cities, self.cityDistances)
        sm = sparse.csr_matrix(m)
        t = sparse.csgraph.minimum_spanning_tree(sm)
        # print self.cityDistances[34][1]
        current_dist = self.cityDistances[int(node.state[len(node.state)-1])][11]
        return sum(t.data) + current_dist


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
def to_adjency(m, from_matrix = None):
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
        for i in range(46):
            problem = TspProblem(48,dataMatrix, tuple([str(i)]))
            result = astar(problem)
            print result
        # problem = TspProblem(48,dataMatrix, tuple(['34']))
        # result = astar(problem)
        # print result

        
if __name__ == '__main__':
        main()    
