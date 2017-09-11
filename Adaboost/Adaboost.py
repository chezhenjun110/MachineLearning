from numpy import *
def loadSimpData():
    datMat = matrix([[1., 2.1],
                     [2., 1.1],
                     [1.3, 1.],
                     [1., 1.],
                     [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq): #输入：样本特征矩阵，指定特征，阈值，是否反转类别
    retarray=ones((shape(dataMatrix)[0],1))
    if threshIneq=='lt':
        retarray[dataMatrix[:,dimen]<=threshVal]=-1.0
    else:
        retarray[dataMatrix[:,dimen]>threshVal]=-1.0
    return retarray
def buildstump(datamatrix,labels,D):
    dataMat=mat(datamatrix)
    classlabels=mat(labels).T
    m,n=shape(dataMat)
    numsteps=10.0
    minerro=inf
    beststump={}
    bestclassest=mat(zeros((m,1)))
    for i in range(n):
        min=dataMat[:,i].min()
        max=dataMat[:,i].max()
        stepsize=(max-min)/numsteps   #步距
        for j in range(-1,int(numsteps)+1):
            for inequal in ['lt', 'gt']:
                threshval=min+float(j)*stepsize
                predictedval=stumpClassify(dataMat,i,threshval,inequal)
                errarr=mat(ones((m,1)))
                errarr[predictedval==classlabels]=0
                weighted=D.T*errarr
                print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshval, inequal, weighted))
                if weighted<minerro:
                    minerro=weighted
                    bestclassest=predictedval.copy()
                    beststump['dimen']=i
                    beststump['thresh']=threshval
                    beststump['threshIneq']=inequal
    return bestclassest,beststump,minerro

