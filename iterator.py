
import random


class RandomIterator:
    def __init__(self, *ele):
        print ele
        self.elements = list(ele)
        print self.elements

    def __iter__(self):
        random.shuffle(self.elements)
        self.cursor=0
        return self

    def next(self):
        if self.cursor >= len(self.elements):
            raise StopIteration()
        e = self.elements[self.cursor]
        self.cursor += 1
        return e



r_itr = RandomIterator(1, 2, 3)

for e in r_itr:
    print e
