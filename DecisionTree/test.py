import DecisonTree as dt
import  treePlotter as tp
dataSet,lables=dt.createDataset()
mytree=tp.retrieveTree(0)
dt.storeTree(mytree,"abc.txt")
#print(dt.loadtree("classifierStorage.txt"))
