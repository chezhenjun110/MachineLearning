import Adaboost as boost
from numpy import *
dataSet,labels=boost.loadSimpData()
retArray=ones((shape(dataSet)[0],1))
#a=shape(dataSet)[0]
print(retArray)