import kNN
from numpy import *
import matplotlib.pyplot as plt
datamatrix,datalables=kNN.file2matrix("datingTestSet2.txt")
#绘制关于坐标轴的图
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(datamatrix[:,1],datamatrix[:,2],15.0* array(datalables),15.0* array(datalables))
# plt.show()
#dataset=kNN.img2matirx("testDigits/0_0.txt")

print(kNN.handClassify())
