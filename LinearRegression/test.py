import regression as re
from numpy import *
import matplotlib.pyplot as plt
dataset,labels=re.LoadData("ex0.txt")
#print(dataset[:10])
#print(labels[:10])
# w=re.getRegression(dataset,labels)
# #print(shape(w))
xmat=mat(dataset)
ymat=mat(labels)
# yhat1=xmat*w
# fig=plt.figure()
# ax=fig.add_subplot(111)      #控制坐标系的大小
# ax.scatter(xmat[:,1].flatten().A[0],ymat.T[:,0].flatten().A[0])    #第一个参数为x轴，第二个为y轴
# xcopy=xmat.copy()
# xcopy.sort(0)       #排序
# yhat=xcopy*w
# print(yhat.T)
# print(ymat)
# print(corrcoef(yhat1.T,ymat))
# ax.plot(xcopy[:,1],yhat)           #构造线段
#plt.show()
print(xmat[1,:])
print(re.lwlr(xmat[0],xmat,ymat,1.0))