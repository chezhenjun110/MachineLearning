import regression as re
from numpy import *
import matplotlib.pyplot as plt
dataset,labels=re.LoadData("abalone.txt")

xmat=mat(dataset)
print(xmat[:5])
regu=re.regularize(xmat)
print(regu)
