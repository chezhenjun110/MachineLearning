from SVM import SMO as smo
dataset,lables=smo.loadDataSet("testSet.txt")
b,alphas=smo.smoSimple(dataset,lables,0.6,0.001,40)
print(b)
print(alphas)
