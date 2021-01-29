"""
Curring is reducing a func with many arg to one arg
passing one argument to a function;

"""

#actual func
def add(a,b,c):
    return a+b+c

#Binding

from functools import partial

add10 = partial(add,10)
add100 = partial(add10,100)
print add100(1000)


#currying:
# add(1,2,3) ==> add(1)(2)(3)
from inspect import signature

def curry(func):
    def inner(arg):
        if len(signature(func).parameters)==1:
            return func(arg)
        return curry(partial(func,arg))
    return

@curry
def add(a,b,c):
    return a+b+c
add10 = add(10)
add100 = add10(100)
print add100(1000)
