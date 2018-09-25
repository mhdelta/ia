#
# SimpleAI Traveling Salesman Problem
# Author: Aaron Hung
# Date: 5/05/15
# Purpose: Traveling Salesman Problem solution using SimpleAI's framework for state space search using Hill Climbing algorithm.
#

from simpleai.search import SearchProblem, hill_climbing_random_restarts, astar
from simpleai.search.viewers import ConsoleViewer
import random
from kruskal import kruskal_min_span_tree, readfile
import math
MIN_DISTANCE = kruskal_min_span_tree(readfile('att48.tsp'))


class TspProblem(SearchProblem):

        def __init__(self, cities, distances):
                '''Traveling Salesman Problem Class Constructor'''
                self.numCities = cities
                self.cityDistances = distances
                self.tour = [1,2,3,4,5,6,7,8,9,10,11]
                super(TspProblem, self).__init__(initial_state=[[0] + random.sample(self.tour, len(self.tour)) + [0]])

        def actions(self, s):
                '''Return action list with action description[0] and resulting tour[1]'''
                actions = []

                x = random.randint(1, self.numCities-1)
                y = random.randint(1, self.numCities-1)

                # Choose 2 random points until valid for reversing tour edge
                while x == y or y == min(x, y):
                        x = random.randint(1, self.numCities-1)
                        y = random.randint(1, self.numCities-1)

                # Reverse edge
                s[0] = s[0][0:x+1] + list(reversed(s[0][x+1:y])) + s[0][y:]

                actions.append(('2-change at ' + str(x) + ' and ' + str(y), s))

                return actions

        def result(self, s ,a):
                '''Return resulting tour from action'''
                return a[1]

        def value(self, s):
                '''Return the length of the tour'''
                return self.__tour_length(s)

        def generate_random_state(self):
                '''Return a random generated tour'''
                return [[0] + random.sample(self.tour, len(self.tour))+ [0]]

        def __tour_length(self, s):
                '''Return length of state or total distance of tour'''
                total_dist = 0

                for i in range (0, self.numCities - 2):
                        current_city = s[0][i]
                        next_city = s[0][i + 1]
                        current_dist = self.cityDistances[current_city][next_city]
                        total_dist += current_dist

                # Add in distance for returning trip to origin of tour
                total_dist += self.cityDistances[s[0][self.numCities - 1]][s[0][0]]

                return total_dist

        def heuristic(self, s):
                return math.fabs(self.__tour_length(s) - MIN_DISTANCE)


problem = TspProblem(12, [12,12,12,12,12])