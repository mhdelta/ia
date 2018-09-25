'''
8 puzzle problem, a smaller version of the fifteen puzzle:
http://en.wikipedia.org/wiki/Fifteen_puzzle
States are defined as string representations of the pieces on the puzzle.
Actions denote what piece will be moved to the empty space.
States must allways be inmutable. We will use strings, but internally most of
the time we will convert those strings to lists, which are easier to handle.
For example, the state (string):
'1-2-3
 4-5-6
 7-8-e'
will become (in lists):
[['1', '2', '3'],
 ['4', '5', '6'],
 ['7', '8', 'e']]
'''

from __future__ import print_function

from simpleai.search import astar, SearchProblem, breadth_first as BFTS, depth_first as DFTS
from simpleai.search.viewers import WebViewer
from datetime import datetime, timedelta
import os



def find_location(rows, element_to_find):
    '''Find the location of a piece in the puzzle.
       Returns a tuple: row, column'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


GOAL = ('n', '.', 'n','.', '.', '.','b', '.', 'b')

class Caballos(SearchProblem):
    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
        preactions = []
        actions = []
        matrix_state = [[],[],[]]
        cont = 0
        for i in range(3):
            l = []
            for j in range(3):
                l.append(state[cont])
                cont += 1
            matrix_state[i] = l
            
        for i in range(3):
            for j in range(3):
                if matrix_state[i][j] != '.':
                    preactions.append([(i, j), (i+2, j+1)])
                    preactions.append([(i, j), (i+2, j-1)])
                    preactions.append([(i, j), (i-2, j+1)])
                    preactions.append([(i, j), (i-2, j-1)])
                    preactions.append([(i, j), (i+1, j+2)])
                    preactions.append([(i, j), (i+1, j-2)])
                    preactions.append([(i, j), (i-1, j+2)])
                    preactions.append([(i, j), (i-1, j-2)])
        for x in preactions:
            valid = True
            for y in x[1]:
                if not(y >= 0 and y < 3):
                    valid = False
            if valid and matrix_state[x[1][0]][x[1][1]] == '.':
                actions.append(x)
        return tuple(actions)

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.
           (the "action" parameter contains the piece to move)
        '''
        newstate = []
        for x in state:
            newstate.append(list(x))
        matrix_state = [[],[],[]]
        cont = 0
        for i in range(3):
            l = []
            for j in range(3):
                l.append(newstate[cont])
                cont += 1
            matrix_state[i] = l
        tmp = matrix_state[action[0][0]][action[0][1]]
        matrix_state[action[0][0]][action[0][1]] = matrix_state[action[1][0]][action[1][1]]
        matrix_state[action[1][0]][action[1][1]] = tmp
        newtuple = tuple()
        for i in range(3):
            for j in range(3):
                newtuple += tuple(matrix_state[i][j])
        return newtuple

    def is_goal(self, state):
        '''Returns true if a state is the goal state.'''
        print (state)
        return state == GOAL

    def cost(self, state1, action, state2):
        '''Returns the cost of performing an action. No useful on this problem, i
           but needed.
        '''
        return 1

    def heuristic(self, state):
        '''Returns an *estimation* of the distance from a state to the goal.
           We are using the manhattan distance.
        '''
        # distance = 10
        #l = list(state)
        #if l[0] == 'n':
        #    distance -= 3
        #if l[2] == 'n':
        #    distance -= 3
        #if l[6] == 'b':
        #    distance -= 3
        #if l[8] == 'b':
        #    distance -= 3
        # print ('state ', state)
        # print ('distance', distance)
        return 1


# result = astar(EigthPuzzleProblem(INITIAL))
# if you want to use the visual debugger, use this instead:
# result = astar(EigthPuzzleProblem(INITIAL), viewer=WebViewer())


med = (('b', '.', 'b', '.', '.', '.', 'n', '.', 'n'))

problem = Caballos(med)
print(astar(problem))
