import itertools
import functools

i=itertools.chain((range(5),range(5,10)))
while i:
    try:
        print i.next()
    except:
        break

print "\n\n"
i=itertools.combinations(range(4), 2)
while i:
    try:
        print i.next()
    except:
        break

print "\n\n"
#cycle thourgh an iterator infintely
i=itertools.cycle(range(5))
while i:
    try:
        j= i.next()
        print j
        if j == 4 : break
    except:
        break

print "\n\n"
i=itertools.chain([1,2,3],'sri')
while i:
    try:
        j= i.next()
        print j
    except:
        break

print "\n\n"
selectors=True,False,True,False
it=itertools.compress(range(4), selectors)
for j in it:
    print j

print "\n\n"
it=itertools.product([0,1,2],[4,5,6],[9,0])
for x,y,z in it:
    print (x,y,z)
