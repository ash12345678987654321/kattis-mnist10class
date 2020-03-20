import random

training=[]
validation=[]

weights=[]


def sign(i):
    if (i>0):
        return 1
    else:
        return -1

def test(epoch_num):
    out=[]

    for i in range(150):
        out.append([])
        out[i]=[sign(x) for x in weights[i]]

    file=open("epoch"+str(epoch_num)+".txt","w")
    for i in range(150):
        for j in range(51):
            file.write(str(out[i][j])+" ")
        file.write("\n")

    file.close()

    correct=0

    print(len(validation))
    for k in range(len(validation)):
        layer1=[0]*150

        for i in range(150):
            for j in range(51):
                layer1[i]+=out[i][j]*validation[k][j]

        layer2=[0]*10

        for i in range(150):
            layer2[i//15]+=sign(layer1[i])

        best=-20
        for i in range(10):
            best=max(layer2[i],best)

        for i in range(10):
            if (best==layer2[i]):
                if (i==validation[k][51]):
                    correct+=1
                break

    print("epoch "+str(epoch_num)+": "+str(correct)+"/"+str(len(validation)))
    

def main():
    global training,validation
    
    file=open("train.txt","r")
    training=[i.split(" ") for i in file.read().split("\n")]
    file.close()
    
    file=open("validation.txt","r")
    validation=[i.split(" ") for i in file.read().split("\n")]
    file.close()

    for i in range(len(training)):
        training[i]=[int(x) for x in training[i]]

    for i in range(len(validation)):
        validation[i]=[int(x) for x in validation[i]]
    
    for i in range(150):
        weights.append([])
        for j in range(51):
            weights[i].append(0) #initalizing weights to all 0

    test(0)

    #weight will be in the range [-1,1]
    #for each output node the goal is to reach 15 or -15 depending on answer

    BATCH_SIZE=100 #perhaps this is a good number


if __name__=="__main__":
    main()
