#List comprehnsion

l=[i*i for i in range(5)]
print l


#Filter comprehension

print [i*10 for i in range(5) if i%2==0]


#Dict Comprehension
print ""
names=["sri","kan","th"]
enum = [1,2,3,4]
val = [11,22,33]

print zip(names,enum)
d=dict(zip(names,enum))
print d
d={n:e for n,e in zip(names,enum)}
print d

for n,e,v in zip(names,enum,val):
    print n,e,v
print ""

print map(lambda i:i*i,enum)
print filter(lambda i: i%2==0,enum)
