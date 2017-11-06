from SVM import SMO as smo
from numpy import  *

dataset,lables=smo.loadDataSet("testSet.txt")

# b,alphas=smo.smoSimple(dataset,lables,0.6,0.001,40)
# print(b)
# print(alphas)
# b,alphas=smo.smoP(dataset,lables,0.6,0.001,40)
# ws=smo.calcWs(alphas,dataset,lables)
# predict=mat(dataset)[2]*mat(ws)+b
# print(dataset[2])
# print(predict)
smo.testDigits(('rbf',20))