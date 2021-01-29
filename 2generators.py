import random

sentence = ["a", "b", "c", "d", "e", "z"]

def send():
    while True:
        yield random.choice(sentence)

def reply():
    while True:
        rcv = yield
        print "received:%r" % rcv
        if rcv == "z":
            break ## raises StopIteration exception
        print "replied %r" % random.choice(sentence)

s=send()
r=reply()

r.send(None)
while True:

    rcv = s.send(None)
    try:
        r.send(rcv)
    except StopIteration:
        break
