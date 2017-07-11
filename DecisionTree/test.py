import DecisonTree as dt
import  treePlotter as tp
#dataSet,lables=dt.createDataset()
#mytree=tp.retrieveTree(0)
#dt.storeTree(mytree,"abc.txt")
#print(dt.loadtree("abc.txt"))
fr=open("lenses.txt")
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lenseslabels=['age','prescipt','astigmatic','tearrate']
lensesTree=dt.createTree(lenses,lenseslabels)
print(lensesTree)
tp.createPlot(lensesTree)
