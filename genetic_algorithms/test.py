import random
DIG = [str(i) for i in range(1,10)]
OP = ['+', '-', '/', '*']
def CreateRandomExpr():
    while True:
        n = random.randint(3, 11)
        if n%2 == 1:
            str = ""
            for i in range(n):
                x = random.randint(0, 8)
                y = random.randint(0, 3)
                if i%2 == 0:
                    str += DIG[x]
                else:
                    str += OP[y]
            return str