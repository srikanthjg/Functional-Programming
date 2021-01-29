#Bidirectional generator



sentence=["yo","wazza","just chillin"]


def randomConversation():

    rcv = yield "hi"
    print rcv + " 1 \n"
    i=2
    for s in sentence:
        r = yield s
        print r + str(i)+"\n"
        i+=1

#first time you have to send a None to recceive the first yield object
#Because generator "Sends before receiving that why we need to send None the first time"


g = randomConversation()

print g.send(None)
print g.send("hola")
