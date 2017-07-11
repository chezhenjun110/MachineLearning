import bayes
import feedparser
# listoftext,labels=bayes.loadDataSet()
# vocalist=bayes.createvocaList(listoftext)
# vec=bayes.setOwords2vec(vocalist,listoftext[1])
# trainMat=[]
# for item in listoftext:
#      trainMat.append(bayes.setOwords2vec(vocalist,item))
# p0v,p1v,pab=bayes.trainNB0(trainMat,labels)
# print(p1v)
#print(bayes.EmailTest())
fp=feedparser.parse("https://newyork.craigslist.org/stp/index.rss")
print(fp)