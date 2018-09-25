#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aima import search
from aima.search import Problem, breadth_first_search as BFTS, depth_first_tree_search as DFTS, astar_search as astar
from aima.search import best_first_graph_search as bfgs
from datetime import datetime, timedelta
from pyfiglet import Figlet
import os
import time
import math
class EightPuzzle(Problem):

    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank. A state is represented as a 3x3 list,
    where element at index i,j represents the tile number (0 if it's an empty square) """
 
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)
    
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)
    
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']       
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
           possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP':-3, 'DOWN':3, 'LEFT':-1, 'RIGHT':1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]
        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i, len(state)):
                if state[i] > state[j] != 0:
                    inversion += 1
        
        return inversion % 2 == 0
    
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))

def animate_8_puzzle(path):
    state_matrix = []
    for i in range(len(path)):
        matrix = []
        matrix.append(path[i].state[0:3])
        matrix.append(path[i].state[3:6])
        matrix.append(path[i].state[6:9])            
        state_matrix.append(matrix)
    for m in state_matrix:
        f = Figlet()
        # os.system('reset') #assuming the platform is linux, clears the screen
        for row in m:
            print( row)
        print ("========")
        time.sleep(1.3)

def h_euclidian(node):
    tmp = node.state
    state = [[], [], []]
    state[0] = tmp[0:3]
    state[1] = tmp[3:6]
    state[2] = tmp[6:8]
    total = 0
    for tup in state:
        for number in tup:
            if number != 0:
                idealx = (number % 3) - 1
                if idealx < 0:
                    idealx = 2
                idealy = (number - 1) // 3
            else:
                idealx = 2
                idealy = 2
            realy = state.index(tup)
            realx = tup.index(number)
            total += float(math.sqrt(math.pow((idealx-realx),2)+math.pow((idealy-realy),2)))
    return total

def h_manhattan(node, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    distance = 0
    kalan = 0
    bolum = 0
    current_state = node.state
    for i in current_state:
        position_difference = abs(goal.index(i) - current_state.index(i))
        if i is not 0:
            kalan = position_difference % 3
            bolum = position_difference / 3
            distance += kalan + int(math.floor(bolum))
            if abs(goal.index(i) % 3 - current_state.index(i) % 3) == 2 and position_difference % 3 == 1:
                distance += 2
            # print "i: " + str(i) + " goal-index: " + str(goal.index(i)) + " current-index: " + str(current_state.index(i)) + " bolum: " + str(bolum) + ": kalan: " + str(kalan) + ": distance: " + str(distance)
    return distance

def h_hamming(node, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    distance = 0
    state_i = node.state
    for i in goal:
        if goal.index(i) - state_i.index(i) != 0 and i != 0:
            distance += 1
    return distance

med = (4,1,2,8,7,3,5,6,0)
worst_case = (8,7,6,5,4,3,2,1,0)
initial_state = (1,2,5,6,8,0,7,4,3)
example_state7 = (8,7,6,5,4,3,2,1,0)

h_funcs = [h_manhattan, h_euclidian, h_hamming]
h_names = ['Distancia Manhattan', 'Distancia Euclidiana', 'Heurística de Hamming']
p_list = [med, initial_state, example_state7, worst_case]

for p in p_list:
    print "================================="
    print "Solving: ", p
    i = 0
    for h in h_funcs:
        print "Using: ", h_names[i]
        problem = EightPuzzle(p)
        t_start = datetime.now()
        result = astar(problem, h)
        t_end = datetime.now()
        delta = t_end - t_start
        total = timedelta.total_seconds(delta)
        movs = len(result.solution())
        print "Time elapsed: ", total
        print "movs: ", movs
        i += 1
