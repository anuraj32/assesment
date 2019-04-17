import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.corpus import sentiwordnet as swn

#create a list neg_word to store the negative words from corpora opinio_lexicon
neg_word=[]
for wor in opinion_lexicon.words("negative-words.txt"): #Fetch the values from negative text file and converted into simple words
	neg_word.append(wor)
#print("Negative words :",neg_word)optional for testing

pos_word=[]
for wos in opinion_lexicon.words("positive-words.txt"):
	pos_word.append(wos)
#print("Positive words :",pos_word)optional for testing

text1='''My mood is so bad''' #take a input
output_word=word_tokenize(text1) #tokenzine into words for further processing as we can not iterate directly to a string

#Create a function for calculating positive and negative words from the input
def calculator(value1):
    # Count positive words
    numPosWords = 0
    for word in output_word:
        if word in pos_word:
            numPosWords += 1
            
    # Count negative words
    numNegWords = 0
    for word in output_word:
        if word in neg_word:
            numNegWords += 1
    #find the accuracy of input
    sum = (numPosWords - numNegWords)
    return sum


pos_neg=calculator(text1)
#To check whether a input line is positive/negative
if pos_neg>0:
	for positive_word in output_word:
		if positive_word in pos_word:
            #if a word in input is present in positive_word database then print that word
			print(positive_word)
else:
	for negative_word in output_word:
		if negative_word in neg_word:
			print(negative_word)
            #if a word in input is present in positive_word database then print that word


