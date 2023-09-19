#-------------------------------------------------------------------------
# AUTHOR: Loc Nguyen
# FILENAME: search_engine.py
# SPECIFICATION: Calculate tf-idf, return doc >=0.1, and calculate precision and recall
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv,math

documents = []
labels = []

#reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])
            #print("[%d]%s" % (i,row))

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}
for word in stopWords:
  for i in range(len(documents)):
    if word in documents[i]:
      documents[i] = documents[i].replace(word,'').strip()

#print(documents)

#Conduct stemming.
#--> add your Python code here
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for keys in stemming:
  for i in range(len(documents)):
    if keys in documents[i]:
      documents[i] = documents[i].replace(keys,stemming[keys])

#print(documents)

#Identify the index terms.
#--> add your Python code here
terms = []
for phrase in documents:
  sentence = phrase.split(' ')
  for word in sentence:
    if word not in terms:
      terms.append(word)

#remove empty strings      
terms = list(filter(None,terms))
#print(terms)

#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []
def findTF(terms, sentence):
  tfDict = {}
  for word in terms:
    wordCount = sentence.count(word)
    tfDict[word] = wordCount
  return tfDict

doc1tf = findTF(terms,documents[0])
doc2tf = findTF(terms,documents[1])
doc3tf = findTF(terms,documents[2])

def findIDF(terms,documents,doc1,doc2,doc3):
  idfDict = {}
  numOfDoc = len(documents)
  wordCount = 0
  for word in terms:
    if doc1[word] > 0:
      wordCount += 1
    if doc2[word] > 0:
      wordCount += 1
    if doc3[word] > 0:
      wordCount += 1
    idfDict[word] = math.log10(numOfDoc/wordCount)
    wordCount = 0
  return idfDict

idf = findIDF(terms,documents,doc1tf,doc2tf,doc3tf)

def findTFIDF(terms,doc1tf,doc2tf,doc3tf,idf):
  tf_idf_Dict = {}
  for word in terms:
    

    

    
    

  

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here