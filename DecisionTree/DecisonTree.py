from math import log
import operator
def createDataset():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # change to discrete values
    return dataSet, labels
def CalcShannonEnt(dataset):
    datasetSize=len(dataset)
    labels={}
    for item in dataset:
        label=item[-1]
        if label not in labels.keys():labels[label]=0
        labels[label]+=1
    shannonEnt=0.0
    for key in labels:
        prob=float(labels[key])/datasetSize
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

def chosebestfeature(dataset):
    featureNum=len(dataset[0])-1          #特征值个数（数据列表中最后一个为label）
    bestfeature=-1;bestgrid=0.0
    baseEnt=CalcShannonEnt(dataset)
    for i in range(featureNum):
        featureList=[example[i] for example in dataset]
        uniqueVals=set(featureList)
        newEnt=0.0
        for v in uniqueVals:
            subdataset=SplitDataSet(dataset,i,v)
            prob=len(subdataset)/float(featureNum+1)
            newEnt +=prob*CalcShannonEnt(subdataset)          #子串的概率*子串的信息熵
            infogain=baseEnt-newEnt               #计算新的信息增益
            if(infogain>bestgrid):
                bestgrid=infogain
                bestfeature=i
        return bestfeature

def SplitDataSet(dataset,axis,value):              #根据特征划分数据集
    returndataset=[]
    for item in dataset:
        if item[axis]==value:
            cache=item[:axis]
            cache.extend(item[axis+1:])
            returndataset.append(cache)
    return returndataset
#多数表决
#当处理完所有的属性后，类标签仍不唯一，通过多数表决定义叶子节点
def majorityCnt(classList):
    classCount = {} #数据字典存储每个类标签出现的频率
    for vote in classCount:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    #按照标签出现的频率降序排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]   #返回出现次数最多的标签
