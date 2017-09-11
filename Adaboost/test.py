import Adaboost as boost
from numpy import *
dataSet,labels=boost.loadSimpData()
retArray=ones((shape(dataSet)[1],1))
#a=shape(dataSet)[0]
D=mat(ones((5,1))/5)
bestclassest,beststump,minerro=boost.buildstump(dataSet,labels,D)
print(bestclassest)
print(beststump)
print(minerro)