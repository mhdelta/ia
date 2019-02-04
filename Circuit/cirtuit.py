import sys
class Connection(object):

    def __init__(self, components = None, desc = ""):
        self.desc = desc
        if components:
            self.components = components
        else:
            self.components = []

class CircuitBreaker(object):

    def __init__(self, amp = 10, connection = None, desc = ""):
        self.desc = desc
        self.amp = amp
        self.state = True
        self.working = True
        self.primaryConnection = connection
        self.name = "Circuit Breaker"

class Switch(object):

    def __init__(self, inner = None, out = None, desc = ""):
        self.desc = desc
        self.inner = inner # Conexiones de entrada
        self.out = out # Conexiones de salida
        self.status = None # Hacia donde esta conectado
        self.name = "Switch"


class EndComponent(object):

    def __init__(self, inner = None, type = "outlet", desc = ""):
        self.desc = desc
        self.inner = inner # Conexiones de entrada
        self.type = type
        self.name = "End Component"


class OutsidePower(object):

    def __init__(self, out, desc = ""):
        self.desc = desc
        self.out = out # Conexiones de salida
        self.name = "Outside Power"


class Circuit(object):

    def __init__(self, connections = None, desc = ""):
        self.desc = desc
        if connections:
            self.connections = connections
        else:
            self.connections = []




# Componentes

s1 = Switch(desc="s1")
s2 = Switch(desc="s2")
s3 = Switch(desc="s3")

l1 = EndComponent(desc="l1")
l2 = EndComponent(desc="l2")

p1 = EndComponent(desc="p1")
p2 = EndComponent(desc="p2")

cb1 = CircuitBreaker(desc="cb1")
cb2 = CircuitBreaker(desc="cb2")

op = OutsidePower([cb1, cb2], desc="op")

w0 = Connection([l1, s2], desc="w0") 
w1 = Connection([s1, s2], desc="w1")
w2 = Connection([s1, s2], desc="w2")
w3 = Connection([cb1, s1, s3, p1], desc="w3")
w4 = Connection([s3, l2], desc="w4")
w5 = Connection([cb1, cb2], desc="w5")
w6 = Connection([cb2, p2], desc="w6")


miCasita = Circuit([w0, w1, w2, w3, w4, w5, w6])

for i in miCasita.connections:
    print "-------------CONEXION " + i.desc + " -------------------"
    for j in i.components:
        print j.name + ": " + j.desc
    print "--------------------------------"
