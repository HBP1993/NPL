import imp

from tracemalloc import stop
from textblob import TextBlob, Word
import nltk
from pathlib import Path

import pandas as pd


#nltk.download("stopwords")
from nltk.corpus import stopwords

stops = stopwords.words("english")
#print(stops)

blob = TextBlob ("Today is a beautiful day.")
print(blob.words) # this is the list, you can iterate through that list 

cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist)



'''20 popular words from the text'''
# make a blob out of the text 
blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.word_counts["juliet"])

# print(blob.word_counts["romeo"])

# print(blob.word_counts["love"])

# print(blob.noun_phrases.count("lady capulet"))



'''add thee, thy, thou to stops'''
more_stops = ["thee", "thy", "thou"]
stops += more_stops

items = blob.word_counts.items()

#print(items) #it produces every words number of times it appeares in text 



# use a list comprehension to eliminate any tuples 
#counting stop words: 
''' eliminate all stop words and tuples '''

items = [i for i in items if i[0] not in stops] # we are looking first word so i[0]

print(items[:10])

from operator import itemgetter

sorted_items = sorted(items)


sorted_items = sorted(items, key = itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]
#df = pd.DataFrame(top20, columns = ["words", "Count"])
df = pd.DataFrame(top20, columns=["words", "Count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="words", y="Count", legend=False)
plt.gcf().tight_layout()

plt.show()