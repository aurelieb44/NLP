from textblob import TextBlob
'''
text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)
#print(blob)

sentences = blob.sentences
#print(sentences)

words = blob.words
#print(words)

#print(blob.tags) # part of speech tag # JJ is adjective
print(blob.noun_phrases) # prints the noun phrases

# SENTIMENT ANALYSIS
#print(blob.sentiment) # how subjective, positive, negative something is between -1 and 1
#print(blob.sentiment.polarity)
#print(blob.sentiment.subjectivity)

for sentence in sentences:
    print(round(sentence.sentiment.polarity,3))

from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer()) 
# gives a classification, a value of how positive and a value for how negative it is. 
# it classifies it as negative but still has some positive in it.
print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)

# LANGUAGE DETECTION AND TRANSLATION

spanish = blob.translate(to='es')
print(spanish)
chinese = blob.translate(to="zh")
print(chinese)
french = blob.translate(to='fr')
print(french)
hindi = blob.translate(to='hi')
print(hindi)
nepali = blob.translate(to='ne')
print(nepali)

english = hindi.translate()
print(english)
'''
from textblob import Word
index = Word('index') # pluralize index
cacti = Word('cacti') # singularize cacti
print(index.pluralize())
print(cacti.singularize())

#wordlist
animals = TextBlob("dog cat fish bird").words
print(animals.pluralize())

#spellcheck and corrections
word = Word("theyr")
print(word.spellcheck()) # show confidence level and check
print(word.correct()) # goes with the one with the highest confidence level

# from nltk.stem import WordNetLemmatizer
word1 = Word('studies')
word2 = Word('varieties')
print(word1.stem())
print(word2.stem())
#print(word1.lemmatize()) # ERROR
#print(word2.lemmatize()) #ERROR

happy = Word('happy')
#print(happy.definitions) # ERROR
#print(happy.synsets) # ERROR