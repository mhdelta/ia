import re

str = "cuales son los mejores juegos del 2018"
listy = ('')
query = '(cuales son| listar| liste| diga) (.*) (mejores|peores) (.*) (de|del) (?P<date>.*)'
o = re.search(query, str)
if o:
    print o.group('date')
    # Output >> 2018 
else:
    print ":("