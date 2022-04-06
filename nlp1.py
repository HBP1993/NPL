from textblob import TextBlob
import nltk

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences

#print(sentences)

words = blob.words 

# print(words)

# print(blob.tags)

#print(blob.noun_phrases)

# print(blob.sentiment)
# print(blob.sentiment.polarity) #it is between -1 to 1
# print(blob.sentiment.subjectivity)

for sentence in sentences:
    print(round(sentence.sentiment.polarity,3))
    
    
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# for sentence in blob.sentences:
#     print(sentence.sentiment)
    

spanish = blob.translate(to = 'es')

print(spanish)

chinese = blob.translate(to='zh')

print(chinese)

french = blob.translate(to = 'fr')

print(french)

hindi = blob.translate(to = 'hi')

print(hindi)

nepali = blob.translate(to = 'ne')

print(nepali)

english = hindi.translate()

print(english)


'''for singular and plural'''

from textblob import Word

index = Word("index")
cacti = Word("cacti")

print(index.pluralize())
print(cacti.singularize())


'''if we have to do for wordlist at the same time'''
animals = TextBlob('dog cat fish bird mouse').words
print(animals.pluralize())


'''spellcheck and corrections'''
word = Word('theyr')
print(word.spellcheck())
#this also show the confidence level and different options what words may be 

print(word.correct())  #this pick word with higher confidence level



'''stemming just takes off some end alphabates but lemmatization corrects the word '''

from nltk.stem import WordNetLemmatizer
word1 = Word('Studies')
word2 = Word('varieties')

print(word1.stem())
print(word2.stem())

# print(word1.lemmatize())
# print(word2.lemmatize())

'''definations, synonyms, antonyms'''

happy = Word("happy")

print(happy.definitions())
