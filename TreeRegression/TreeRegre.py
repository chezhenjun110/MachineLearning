from numpy import *
def SplitDataset(dataset,feat,value):
    mat0=dataset[nonzero(dataset[:,feat]>value)[0],:][0]
    mat1 = dataset[nonzero(dataset[:, feat] <= value)[0], :]
    return mat0,mat1
def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float,curLine))              #fltLine2=[float(x) for x in curLine]
        dataMat.append(fltLine)
    return dataMat
def regErr():
    pass
def regleaf():
    pass
def chooseBestsplit(dataset,leaftype=regleaf,errtype=regErr,ops=(1,4)):
    pass