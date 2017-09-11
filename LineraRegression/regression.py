from numpy import *
def LoadData(filename):
    fr=open(filename)
    DataSet=[]
    Labels=[]
    datasize= len(fr.readline().split('\t'))-1
    for line in fr.readlines():
        datas=line.strip().split('\t')
        Labels.append(float(datas[-1]))
        curlinedata=[]
        for i in range(datasize):
            curlinedata.append(float(datas[i]))
        DataSet.append(curlinedata)
    return DataSet,Labels
def getRegression(X,y):
    Xmat=mat(X)
    ymat=mat(y)
    Xvalue=Xmat.T*Xmat
    if linalg.det(Xvalue)==0.0:
        print("不可逆！")
        return
    w=Xvalue.I*(Xmat.T*ymat.T)
    return w

def lwlr(testPoint,X,y,k):
    Xmat = mat(X)
    ymat = mat(y).T
    weight=mat(eye((len(Xmat))))
    for i in range(len(Xmat)):
        diff=testPoint-Xmat[i,:]
        weight[i,i]=exp(diff*diff.T/(-2.0*k**2))
    Xvalue = Xmat.T *(weight* Xmat)
    if linalg.det(Xvalue) == 0.0:
        print("不可逆！")
        return
    w = Xvalue.I * (Xmat.T *(weight* ymat))
    return testPoint*w
def lwlrTest(testArr,X,y,k=1.0):
    m=shape(testArr)[0]
    yhat=zeros(m)
    for i in range(m):
        yhat[i]=lwlr(testArr[i],X,y,k)
    return yhat
def rssError(y,yhat):
    return ((y-yhat)**2).sum()
def ridgeRegre(xmat,ymat,lam=0.2):

    xValue=xmat.T*xmat
    denom=xValue+eye(shape(xmat)[1])*lam
    if linalg.det(denom)==0.0:
        print("不可逆！")
    w=denom.I*(xmat.T*ymat)
    return w
def ridgeTest(xArr,yArr):
    xMat = mat(xArr); yMat=mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean     #to eliminate X0 take mean off of Y
    #regularize X's
    xMeans = mean(xMat,0)   #calc mean then subtract it off
    xVar = var(xMat,0)      #calc variance of Xi then divide by it
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegre(xMat,yMat,exp(i-10))
        wMat[i,:]=ws.T
    return wMat
def regularize(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat,0)   #calc mean then subtract it off
    inVar = var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat