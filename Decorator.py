"""
Decorators are wrapper of a function.
Modifies the behaviour of a function
"""

#https://dev.to/apcelent/python-decorator-tutorial-with-example-529f

##1
def check(func):
    def inner(a,b,c):
        if b==0:
            print "Error division by 0"
            return
        print "a/b=",
        return func(a,b)

    return inner

@check
def div(a,b):
    return a/b

arg_doesnt_matter=""
print div(4,2,arg_doesnt_matter)
