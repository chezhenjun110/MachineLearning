from numpy import *
import operator
from os import listdir
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group,labels
# 将数据文件中的数据转化为矩阵
def file2matrix(filename):
    fs=open(filename)
    arraylines=fs.readlines()
    datasize=len(arraylines)
    returnmat=zeros((datasize,3))
    lables=[]
    index=0
    for line in arraylines:
        data=line.strip()
        datas=data.split('\t')
        returnmat[index,:]=datas[0:3]
        lables.append(int(datas[-1]))
        index+=1
    return returnmat,lables
def img2matirx(filename):          #将图像数据读到矩阵中
    fs=open(filename)
    returnMatrix=zeros((1,1024))
    for i in range(32):
        lines=fs.readline()
        for j in range(32):
            returnMatrix[0,32*i+j]=int(lines[j])
    return  returnMatrix
def handClassify():
    trainfiles=listdir("trainingDigits")
    trainDataSize=len(trainfiles)
    trainDataSet = zeros((trainDataSize,1024))
    trainLables=[]
    for i in range(len(trainfiles)):
        trainDataSet[i,:]=img2matirx('trainingDigits/%s'%trainfiles[i])
        lable=int(trainfiles[i].split(".")[0].split("_")[0])
        trainLables.append(lable)
    testfiles = listdir("testDigits")
    testDataSize=len(testfiles)
    testDataSet = zeros((testDataSize, 1024))
    erroCount=0.0
    for i in range(testDataSize):
        vectorundertest = img2matirx('testDigits/%s'%testfiles[i])
        lable = int(testfiles[i].split(".")[0].split("_")[0])
        guessResult=classify0(vectorundertest,trainDataSet,trainLables,3)
        if(guessResult!=lable):
            erroCount+=1.0
        print("I guess the number is %d,and really it is %d"%(guessResult,lable))
    print("erro count is %d"%(erroCount))
def autonorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))  # element wise divide
    return normDataSet, ranges, minVals
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]              #计算数据集的行数
    cache=tile(inX,(dataSetSize,1))
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2                     #计算矩阵的平方
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()  ##argsort()根据元素的值从大到小对元素进行排序，返回下标
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autonorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print (errorCount)
def classifyPerson():
    resultList=['not at all','a small doses','a large doses']
    persentTats=float(input("video games?"))
    ffMiles=float(input("frequent flier miles?"))
    iceCream=float(input("ice cream?"))
    dataset,datalables=file2matrix("datingTestSet2.txt")
    normdataset,ranges,minvalue=autonorm(dataset)
    intArr=array([persentTats,ffMiles,iceCream])
    classifresult=classify0((intArr-minvalue)/ranges,normdataset,datalables,3)
    print(resultList[classifresult-1])
