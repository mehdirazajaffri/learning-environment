"""
nametuple is introduced to assign more meaning to each position of a tuple. 
it returns a tuple with names for each position in the tuple.
"""

from collections import namedtuple, OrderedDict, defaultdict

Direction = namedtuple('Direction','N,S,E,W')
dt = Direction(4,74,0,0)
print(dt)

""" An OrderedDict is a kind of dict that remembers 
the order they are inserted in. In the new version of Python,
the inbuilt dict can remember it too.
"""

dictt = OrderedDict()
dictt['a'] = 5
dictt['d'] = 2
dictt['c'] = 1
dictt['b'] = 3
print(dictt)

"""
A defaultdict will return a default value for the key 
that is not present in the dictionary rather than showing a key error.
"""

dictt = defaultdict(int)
dictt['a'] = 2
print(dictt['a'])  ## return the value
print(dictt['b'])  ## returns the default value