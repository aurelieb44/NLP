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
#my_list = [i for i in nyc_trends[0]['trends']]

for trend in nyc_trends[0]['trends']:
    if trend['tweet_volume']:
        print(trend['tweet_volume'])
        trend = trend['name']
        something = trend['tweet_volume']
        trends.append(trend)
        #volumes.append(volume)

print(trends[:10])
#print(volumes[:10])
trend_volume = zip(trends, volumes)
'''

sorted_tv = sorted(trend_volume, key=itemgetter(1), reverse=True) # reverse=True for descending order # by the count
top10 = sorted_tv[:10]
df = pd.DataFrame(top10,columns=["Tweet", "Volume"])
print(df)

df.plot.bar(x="Tweet",y="Volume", legend=False)
plt.gcf().tight_layout()
plt.show()

'''

# WORDCLOUD

#for tuple in 

text = Path('RomeoAndJuliet.txt').read_text()
mask_image = imageio.imread("mask_oval.png") # if you don't specify the image, it does a rectangular box
wordcloud = WordCloud(colormap="prism",mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text) # ASKKKK
wordcloud = wordcloud.to_file("tweet_cloud.png")
plt.imshow(wordcloud)
plt.show()
print("done")