from numpy import *

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not   
    return postingList,classVec
                 
def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    
    numWords = len(trainMatrix[0])
    
    pAbusive = sum(trainCategory)/float(numTrainDocs)#sum=1+1+1 
    p0Num = zeros(numWords); p1Num = zeros(numWords)      #change to ones() 
    
    p0Denom = 0.0; p1Denom = 0.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
           
    p1Vect = p1Num/p1Denom          #change to log()
    p0Vect = p0Num/p0Denom          #change to log()
    return p0Vect,p1Vect,pAbusive

def getResult(listPost,listClasses):
    trainMat=[]
    list=createVocabList(listPost)
    for postinDoc in listPost:        
        trainMat.append(setOfWords2Vec(list,postinDoc))
        
    p0v,p1v,pAb=trainNB0(trainMat,listClasses)
#     print p0v.index(max(p0v))
    
    print p1v
    print max(p1v)
    print list
if __name__=='__main__':
    postingList,classVec=loadDataSet()
       
    
    getResult(postingList,classVec)
#   print setOfWords2Vec(createVocabList(postingList),postingList[0])
     