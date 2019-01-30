class Connection(object):
    def __init__(self, components = None):
        if components:
            self.components = components
        else:
            self.components = []

class CircuitBreaker(object):
    def __init__(self, amp = 10, connection = None):
        self.amp = amp
        self.state = true
        self.working = true
        self.primaryConnection = connection

class Switch(object):
    def __init__(self, in = None, out = None):
        self.in = in # Conexiones de entrada
        self.out = out # Conexiones de salida
        self.status = None # Hacia donde esta conectado

class EndComponent(object):
    def __init__(self, in = None, type = "outlet"):
        self.in = in # Conexiones de entrada
        self.type = type

class OutsidePower(object):
    def __init__(self, out):
        self.out = out # Conexiones de salida

class Circuit(object):
    def __init__(self, connections = None):
        if connections:
            self.connections = connections
        else:
            self.connections = []




# Componentes

s1 = new Switch()
s2 = new Switch()
s3 = new Switch()

l1 = new EndComponent()
l2 = new EndComponent()

p1 = new EndComponent()
p2 = new EndComponent()

cb1 = new CircuitBreaker()
cb2 = new CircuitBreaker()

op = new OutsidePower([cb1, cb2])

w0 = new Connection([l1, s2]) 
w1 = new Connection([s1, s2])
w2 = new Connection([s1, s2])
w3 = new Connection([cb1, s1, s3, p1])
w4 = new Connection([s3, l2])
w5 = new Connection([cb1, cb2])
w6 = new Connection([cb2, p2])


miCasita = new Circuit([w0, w1, w2, w3, w4, w5, w6])
