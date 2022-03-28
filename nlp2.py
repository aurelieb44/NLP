from typing import Text
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd


#nltk.download("stopwords") # can comment out after it's done, it's only a one time thing
from nltk.corpus import stopwords

stops = stopwords.words("english")
print(stops)
blob = TextBlob("Today is a beautiful day.")
print(blob.words)

# produce a clean list without stopwords and sentences
cleanlist = [word for word in blob.words if word not in stops]
print(cleanlist) # only shows today, beautiful and day

# ROMEO AND JULIET
blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())
print(blob.word_counts["juliet"])
print(blob.word_counts["romeo"])
#print(blob.noun_phrases.count('lady capulet')) # commented out because very slow

more_stops = ["thee", "thy", "thou", "’"]
stops += more_stops

items = blob.word_counts.items()
#print(items)

# use a list comprehension to eliminate any tuples containing stop words:
items = [i for i in items if i[0] not in stops]
print(items[:10]) # thee was eliminated

# top 20 show at the top
from operator import itemgetter
sorted_items = sorted(items)
print(sorted_items[:10]) # alphabetical, by the word, not by the count
sorted_items = sorted(items, key=itemgetter(1), reverse=True) # reverse=True for descending order # by the count
top20 = sorted_items[:20]
df = pd.DataFrame(top20,columns=["words", "Count"])
print(df)

import matplotlib.pyplot as plt
df.plot.bar(x="words",y="Count", legend=False)
plt.gcf().tight_layout()
plt.show()