import math

def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    
    labelCounts={}

    for featVec in dataSet:
        currentLabel=featVec[-1]
       
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0        
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    
    for key in labelCounts:
         
         prob =float(labelCounts[key])/numEntries        
         shannonEnt-=prob*math.log(prob,2)

    return shannonEnt           
    

def createDataSet():
    
    dataSet=[[1,0,'man'],[1,1,'man'],[0,1,'man'],[0,0,'women']]
    labels=['throat','mustache']
    return dataSet,labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting            
            reducedFeatVec.extend(featVec[axis+1:])      
            retDataSet.append(reducedFeatVec)          
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
       
        uniqueVals = set(featList)       #get a set of unique values
        
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

     

def getResult():
    dataSet,labels=createDataSet()
   #  splitDataSet(dataSet,1,1)
    chooseBestFeatureToSplit(dataSet)
    print  chooseBestFeatureToSplit(dataSet)
    #print calcShannonEnt(dataSet)
    

if __name__=='__main__':
   
     
    getResult()    

