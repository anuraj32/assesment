import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import opinion_lexicon
from nltk.corpus import sentiwordnet as swn


neg_word=[]
for wor in opinion_lexicon.words("negative-words.txt"):
	neg_word.append(wor)
#print("Negative words :",neg_word)

pos_word=[]
for wos in opinion_lexicon.words("positive-words.txt"):
	pos_word.append(wos)
#print("Positive words :",pos_word)

text1='''My mood is so bad'''
output_word=word_tokenize(text1)


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

    sum = (numPosWords - numNegWords)
    return sum


pos_neg=calculator(text1)

if pos_neg>0:
	for positive_word in output_word:
		if positive_word in pos_word:
			print(positive_word)
else:
	for negative_word in output_word:
		if negative_word in neg_word:
			print(negative_word)


