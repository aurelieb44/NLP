from typing import Text
from numpy import integer
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
from wordcloud import WordCloud
import imageio
from operator import itemgetter
import matplotlib.pyplot as plt
from nyc_trends import nyc_trends 

trends = []
volumes = []

for trend in nyc_trends[0]['trends']:
    if trend['tweet_volume']:
        #print(trend['tweet_volume'])
        name = trend['name']
        #url = trend['url']
        #query = trend['query']
        #promoted = trend['promoted_content']
        vol = trend['tweet_volume']
        #print(vol)
        trends.append(name)
        volumes.append(vol)

print(trends[:10])
print(volumes[:10])

trend_volume = list(zip(trends, volumes))
print(trend_volume)

sorted_tv = sorted(trend_volume, key=itemgetter(1), reverse=True) # reverse=True for descending order # by the count
top10 = sorted_tv[:10]
df = pd.DataFrame(top10,columns=["Tweet", "Volume"])
print(df)

df.plot.bar(x="Tweet",y="Volume", legend=False)
plt.gcf().tight_layout()
#plt.show()

# WORDCLOUD

df2 = pd.DataFrame(sorted_tv,columns=["Tweet", "Volume"])
a = df2["Volume"] >= 20000
df3 = df2[a]
print('yyy')
print(df3)

text = dict(zip(df3['Tweet'].tolist(), df3['Volume'].tolist()))
wordcloud = WordCloud(colormap="prism",background_color="white", relative_scaling=0.)
wordcloud = wordcloud.generate_from_frequencies(text)
wordcloud = wordcloud.to_file("tweet_cloud.png")

plt.axis("off")
plt.figure(figsize=(40,20))
plt.tight_layout(pad=0)
plt.imshow(wordcloud, interpolation='bilinear')
wordcloud = wordcloud.to_file("tweet_cloud.png")
plt.show()

print("done")
