def fibon(limit):
  a,b = 0,1
  while a < limit:
      yield a
      a, b = b, a + b

for x in fibon(10):
#    print (x)
    pass


def count(range=10):
    a = 0
    while a < range:
        yield a
        a += 1
for i in count():
    pass
    # print(i)

class Counter:
    def __init__(self, start,end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value > self.end:
            raise StopIteration
        curr = self.value
        self.value += 1
        return curr

for i in Counter(10,20):
    print(i)
        