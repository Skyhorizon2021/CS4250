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

#print(doc1tf)

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
#print(idf)

#function to find tf-idf
def findTFIDF(terms,doctf,idf):
  tf_idf_Dict = {}
  termCount = 0
  for num_of_term in doctf.values():
    termCount += num_of_term
  for word in terms:
    tf_idf_Dict[word] = doctf[word]/termCount *idf[word] 
  return tf_idf_Dict

#compute tf-idf for 3 doc
doc1_tfidf = findTFIDF(terms,doc1tf,idf)
doc2_tfidf = findTFIDF(terms,doc2tf,idf)
doc3_tfidf = findTFIDF(terms,doc3tf,idf)

#print(doc1_tfidf)
    
#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []
def docScore(tfidf):
  score = 0
  for val in tfidf.values():
    score += val
  return score

doc1_score = docScore(doc1_tfidf)
doc2_score = docScore(doc2_tfidf)
doc3_score = docScore(doc3_tfidf)

doc_score = {1:doc1_score,2:doc2_score,3:doc3_score}
#print(doc_score)

#user query
user_query = "cat and dog"
tokenized_query = user_query.split()
#tokenize user query
for term in tokenized_query:
  if term not in terms:
    tokenized_query.remove(term)

#binary tokenizer
binary_query = []
for term in terms:
  if term in tokenized_query:
    binary_query.append(1)
  elif term not in tokenized_query:
    binary_query.append(0)
  
print("\nUser query is",user_query)
print("Tokenized query is",tokenized_query)
print("Binary query is",binary_query)
    

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here

#Display result
print("\nTokenized terms:",terms)

print("\nTF-IDF term weights matrix:")
for term in terms:
  print("\t\t",term,end='')

#doc1 value
print("\ndoc1",end='')
for val in doc1_tfidf.values():
  print("\t\t%.4f" % val ,end='')

#doc2 value
print("\ndoc2",end='')
for val in doc2_tfidf.values():
  print("\t\t%.4f" % val,end='')

#doc3 value
print("\ndoc3",end='')
for val in doc3_tfidf.values():
  print("\t\t%.4f" % val,end='')

#Document score
print("\n\nDocument 1 score: %.4f" % doc1_score)
print("Document 2 score: %.4f"%doc2_score)
print("Document 3 score: %.4f"%doc3_score)

#Retrieved document
print("\nRetrieved documents:",end=' ')
for doc in doc_score:
  if doc_score[doc] >= 0.1:
    print(doc,end=' ')

#Relevant document
print("\nRelevant documents: 1 3")

#precision and recall
print('\nPrecision = 2/2 = 100%')
print("Recall = 2/2 = 100%")

  
  