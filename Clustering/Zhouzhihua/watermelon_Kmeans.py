from numpy import *
import random
random.seed()
def txt2mat(filename):
    resultList=[]
    labels=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines:
            data=line.split(" ")
            t=[]
            t.append(float(data[0]))
            t.append(float(data[1]))
            resultList.append(t)
            labels.append(data[2])
    return mat(resultList),mat(labels)
def distvector(vecA,vecB):
    return sqrt(sum(power(vecA - vecB, 2)))
def k_means(dataset,k):
    unchanged=True
    center = zeros((k, 2))
    for i in range(k):
        center[i] = dataset[random.randint(0, 29)]
    label = zeros((len(dataset), 1))
    print(center)
    while unchanged:
        for i in range(len(dataset)):
            cache = inf
            for j in range(k):
                dist = distvector(dataset[i, :], center[j, :])
                if dist < cache:
                    cache = dist
                    label[i] = j
        for i in range(k):
            test = []
            for j in range(len(dataset)):
                if label[j] == i:
                    test.append(dataset[j])
            newcenter = mean(test, axis=0)
            print(newcenter)
            if (newcenter[0]==center[i]).all(): unchanged=False
            center[i] = newcenter
    return center,label
datamatrix,labels=txt2mat("watermelon4.0.txt")
a,b=k_means(datamatrix,2)
aaa=zeros((len(datamatrix),2))
aaa[:,0]=b.T
print(shape(labels))
aaa[:,1]=labels
print(aaa)