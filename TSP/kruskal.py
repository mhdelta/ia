import sys
import platform
import heapq
# if platform.system() == 'Linux':
#     sys.path.insert(0, '/home/mrfreedeer/aima-python')
# else:
#     sys.path.insert(0, 'C://Users//Usuario1//aima-python')
from aima.search import *
import math
import heapq

def euclidian_distance2(pointa, pointb):
    deltax = pointa[0] - pointb[0]
    deltay = pointa[1] - pointb[1]

    return math.sqrt(math.pow(deltax,2) + math.pow(deltay,2))

def euclidian_distance(pointa, pointb):
    deltax = pointa[0] - pointb[0]
    deltay = pointa[1] - pointb[1]
    rij = math.sqrt((math.pow(deltax,2) + math.pow(deltay,2))/10)
    tij = round(rij)
    if(tij < rij):
        dij = tij + 1
    else:
        dij = tij
    return dij

class Edge(object):
    def __init__(self, nodea, nodeb, weight):
        self.minvertex = min(nodea, nodeb)
        self.maxvertex = max(nodea, nodeb)
        self.weight = weight
    def __eq__(self, other):
        return [self.minvertex, self.maxvertex] == [other.minvertex, other.maxvertex]
    def __lt__(self,other):
        return self.weight < other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    def __gt__(self,other):
        return self.weight > other.weight
    def __ge__(self, other):
        return self.weight >= other.weight
    def __str__(self):
        string = ''
        string += 'minvertex: ' + str(self.minvertex) + '\n'
        string += 'maxvertex: ' + str(self.maxvertex) + '\n'
        string += 'weight: ' + str(self.weight)
        return string
class DirectedEdge(object):
    def __init__(self, nodea, nodeb, weight):
        self.startvertex = nodea
        self.targetvertex = nodeb
        self.weight = weight
    def __eq__(self, other):
        return [self.startvertex, self.targetvertex] == [other.startvertex, other.targetvertex]
    def __lt__(self,other):
        return self.weight < other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    def __gt__(self,other):
        return self.weight > other.weight
    def __ge__(self, other):
        return self.weight >= other.weight
    def __str__(self):
        string = ''
        string += 'startvertex: ' + str(self.startvertex) + '\n'
        string += 'targetvertex: ' + str(self.targetvertex) + '\n'
        string += 'weight: ' + str(self.weight)
        return string
class TSPGraph(object):
    def __init__(self, vertexdict,type = 'weird', edges = None):
        if type == 'weird':
            self.graph = {'vertices' : vertexdict}
            edges = []
            for x in self.graph['vertices']:
                point = self.graph['vertices'][x]
                for y in self.graph['vertices']:
                    if x != y:
                        distance = euclidian_distance(point, self.graph['vertices'][y])
                        e = Edge(x,y,distance)
                        # print(e)
                        # input('.')
                        if e not in edges:
                            heapq.heappush(edges, e)
        elif type == 'explicit':
            edges = []
            self.graph = {'vertices' : vertexdict}
            for x in self.graph['vertices']:
                for y in self.graph['vertices'][x]:
                    #print(y, "--")
                    e = Edge(x,y[0],y[1])
                    heapq.heappush(edges,e)
        self.graph['edges'] = edges

    def getVertices(self):
        return list(self.graph['vertices'].keys())
    def getEdges(self):
        return self.graph['edges']
    def getDistance(self,nodea,nodeb):
        return self.graph['edges'][(min(nodea,nodeb), max(nodea,nodeb))]

def kruskal_min_span_tree(graph, type = 'weird'):
    edges = graph.getEdges()[:]
    vertices = graph.getVertices()[:]
    print(len(vertices))
    totalvertices = len(vertices)
    visited = []
    totaldistance = 0
    tree = []
    if type == 'weird':
        while len(visited) != len(vertices):
            minedge = heapq.heappop(edges)
            if not(minedge.minvertex in visited and minedge.maxvertex in visited):
                tree.append(minedge)
                totaldistance += minedge.weight
                if minedge.minvertex not in visited:
                    visited.append(minedge.minvertex)
                if minedge.maxvertex not in visited:
                    visited.append(minedge.maxvertex)
    elif type == 'explicit':
        while len(visited) != len(vertices):
            minedge = heapq.heappop(edges)
            if not(minedge.startvertex in visited and minedge.targetvertex in visited):
                tree.append(minedge)
                totaldistance += minedge.weight
                if minedge.startvertex not in visited:
                    visited.append(minedge.startvertex)
                if minedge.targetvertex not in visited:
                    visited.append(minedge.targetvertex)
    return (tree, totaldistance)


def readfile(filename, type = 'weird'):
    graph = {}
    if type == 'weird':
        with  open(filename) as f:
            line = ''
            for line in f:
                line = line.split()
                # print(line)
                # input('.')
                if 'NODE_COORD_SECTION' in line:
                    break
            for line in f:
                if 'EOF' not in line:
                    split = line.split()
                    numbers = []
                    for thing in split:
                        numbers.append(int(thing))
                    graph[numbers[0]] = (numbers[1], numbers[2])
    elif type == 'explicit':
        with  open(filename) as f:
            line = ''
            for line in f:
                line = line.split()
                # print(line)
                # input('.')
                if 'EDGE_WEIGHT_SECTION' in line:
                    break
            i = 1
            j = 2
            for line in f:
                if 'EOF' in line or 'DISPLAY_DATA_SECTION' in line:
                    break
                numbers = []
                split = line.split()
                for thing in split:
                    numbers.append((j, int(thing)))
                    j += 1
                graph[i] = numbers
                i += 1
                j = i + 1
    # for x in graph:
    #     print(x,"\n\n", graph[x])
    return TSPGraph(graph,type)

def main():
    g = readfile('att48.tsp')
    #print(g.getEdges())
    minspantree = kruskal_min_span_tree(g)
    print(minspantree[1])
    # for x in minspantree[0]:
    #     print(x)
if __name__ == '__main__':
    main()