from numpy import *
import re
import codecs
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec
def createvocaList(dataset):
    vocaList=set([])
    for item in dataset:
        vocaList=vocaList|set(item)
    return list(vocaList)
def setOwords2vec(vocaList,inputset):            #词集模型
    returnvec=[0]*len(vocaList)
    for word in inputset:
        if word in vocaList:
            returnvec[vocaList.index(word)]=1
        else:print("not")
    return returnvec
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num / p1Denom)
    p0Vect = log(p0Num / p0Denom)
    return p0Vect,p1Vect,pAbusive
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0=sum(vec2Classify*p0Vec)+log(1.0-pClass1)
    if p1>p0:
        return 1
    else:
        return 0
def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createvocaList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOwords2vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOwords2vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOwords2vec(myVocabList, testEntry))
    print (testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
def bagOwords2vec(vocaList,inputset):                  #词袋模型
    returnvec=[0]*len(vocaList)
    for word in inputset:
        if word in vocaList:
            returnvec[vocaList.index(word)]+=1
    return returnvec
def textParse(bigString):  # input is big string, #output is word list
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]
def EmailTest():
    docList = [];
    classList = [];
    fullText = []
    for i in range(1, 26):
        word=codecs.open('email/spam/%d.txt' % i,"r",encoding="utf-8").read()
        wordList = textParse(word)
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        word=codecs.open('email/ham/%d.txt' % i,"r",encoding="utf-8").read()
        wordList = textParse(word)
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocaList=createvocaList(fullText)
    trainingSet = list(range(50));
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0
        trainMat.append(bagOwords2vec(vocaList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOwords2vec(vocaList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print ("classification error",docList[docIndex])
    print ('the error rate is: ',float(errorCount)/len(testSet))