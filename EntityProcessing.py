summariesFile=open('./data/summariesOnCheque.txt','r')
stopwordsFile=open('./data/stopWords.txt','r')
wordsFreqFile=open('./data/sortedwordcountCheque.txt','r')
#chequeEntityFile=open('./data/ChequeEntity.txt','w')
#chequeEntityFile2=open('./data/ChequeEntity2.txt','w')
#chequeEntityFile3=open('./data/ChequeEntity3.txt','w')
chequeEntityFile4=open('./data/ChequeEntity4.txt','w')

stopWords=""
#stopWords=stopwordsFile.read().split(',')
for line in stopwordsFile:
    line = line.lower()
    stopWords += line

print(stopWords)

wordsFreqDict=dict()

for line in wordsFreqFile:
    temp=line.split()
    word=temp[0].lower()
    freq=int(temp[1])
    wordsFreqDict[word]=freq

import operator
k=0
entityKeydict=dict()
for line in summariesFile:
    line=line.lower()
    entities=dict()
    for word in line.split():
        #word=word.lower()
        if((stopWords.__contains__(word) or word=='(' or word=='-' or word==':' or word==')') ):
            continue
            #newLine+=word+" "
        else:
            freq=int(wordsFreqDict.get(word,'0'))
            if(freq>0):
                entities[word]=freq

    sorted_Entities = sorted(entities.items(), key=operator.itemgetter(1))
    i=0

    topThreeEntites=list()
    for tup in sorted_Entities:
        topThreeEntites.insert(i,tup[0])
        i=i+1
        if(i==3):
            break
#    i=1
    dupLine="- "
    dupLine2="- "
    k=0
    for word in line.split():
        #lowerword=word.lower()
        if(word in topThreeEntites):
            if(word in entityKeydict.keys()):
                dupLine+='['+word+']'+'('+"key"+str(entityKeydict[word])+') '
                dupLine2 += '[' + word + ']' + '(' + "key" + str(entityKeydict[word]) + ') +'

                line = line.replace(word, "[" + word + "]" + "(" + "key" + str(entityKeydict[word]) + ")", 1)  # i chhanged to k
            else :
                entityKeydict[word]=k
                dupLine+='['+word+']'+'('+"key"+str(entityKeydict[word])+') '
                dupLine2 += '[' + word + ']' + '(' + "key" + str(entityKeydict[word]) + ') +'
                line=line.replace(word,"["+word+"]"+"("+"key"+str(k)+")",1)#i chhanged to k
                k=k+1
            topThreeEntites.remove(word)
            #i=i+
            # k=k+1
#    chequeEntityFile.write(line)
#    chequeEntityFile2.write(line)
#    chequeEntityFile3.write(line)
    chequeEntityFile4.write(line)

    chequeEntityFile4.write(dupLine)
    chequeEntityFile4.write('\n')
    chequeEntityFile4.write(dupLine2)
    chequeEntityFile4.write('\n')






summariesFile.close()
stopwordsFile.close()
wordsFreqFile.close()
chequeEntityFile4.close()