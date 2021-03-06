from aima import search
from aima.search import Problem, breadth_first_search as BFTS, depth_first_tree_search as DFTS, astar_search as astar
from datetime import datetime, timedelta
from pyfiglet import Figlet
import os
import time
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
	"""Describes the distance that would take moving with the minimun distance vector, totally
	differente to manhattan distance"""
    state = node.state
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

def state_to_spirallist(state):
    spiralstate = []
    for x in range(3):
        spiralstate.append(state[0][x])
    spiralstate.append(state[1][2])
    spiralstate.append(state[2][2])
    for x in range(2):
        spiralstate.append(state[2][1-x])
    spiralstate.append(state[1][0])
    spiralstate.append(state[1][1])
    return spiralstate

def state_to_spiralstate(state):
    spirallist = state_to_spirallist(state)
    finalstate = []
    l = []
    for i in range(3):
        if (i % 3) == 0:
            finalstate.append(tuple(l))
            l = []
        l.append(spirallist[i])
    return tuple(finalstate)

def h_sequential_sum(node):
    state = node.state
    end = False
    total = 0
    i = 1
    splist = state_to_spirallist(state)
    if splist[:-1] != 0:
        total += 1
    for x in range(1,8):
        if splist[x] != i+1:
            total += 2
        i += 1
    if splist[0] != 1:
        total += 2
    return total


def h_manhattan(node):
	"""Does not allow diagonal move, only horizontally or vertically"""
    state = node.state
    rowsoff = 0
    colsoff = 0
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
            rowsoff += math.fabs(realy-idealy)
            colsoff += math.fabs(realx-idealx)
    return colsoff + rowsoff

def h_hamming(node):
    state = node.state
    wrong = 0
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
            if [realx, realy] != [idealx, idealy]:
                wrong += 1
    return wrong

def h_Nilsson(node):
return h_manhattan(node) + h_sequential_sum(node)

med = (4,1,2,8,7,3,5,6,0)
problem = EightPuzzle(med)
t_start = datetime.now()
result = BFTS(problem)
t_end = datetime.now()
delta = t_end - t_start
total = timedelta.total_seconds(delta)
#Allows comparation between breath first and depth first search
animate_8_puzzle(result.path())

print( "Breadth first Time elapsed: " , total, " seconds") 
print( "# de movimientos: ", len(result.solution()))
print( "-------------------------------------------------")

t_start = datetime.now()
result = DFTS(problem)
t_end = datetime.now()
delta = t_end - t_start
total = timedelta.total_seconds(delta)

animate_8_puzzle(result.path())

print( "Depth first Time elapsed: " , total, " seconds") 
print( "# de movimientos: ", len(result.solution()))
print( "-------------------------------------------------")
