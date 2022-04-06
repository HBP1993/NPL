from nyc_trends import nyc_trends 
from operator import itemgetter
import matplotlib.pyplot as plt
import pandas as pd

topicTrends = []
tweetVolumes = []

for trend in nyc_trends[0]['trends']:
    if trend['tweet_volume']:
        topicTrends.append(trend['name'])
        tweetVolumes.append(trend['tweet_volume'])


trend_volume = list(zip(topicTrends, tweetVolumes))


storedTopic = sorted(trend_volume, key=itemgetter(1), reverse=True) 
top10 = storedTopic[:10]
df = pd.DataFrame(top10,columns=["Tweet", "Volume"])
df.plot.bar(x="Tweet",y="Volume", legend=False)
plt.gcf().tight_layout()

plt.show()


'''Word Cloud of all topics with over 20,000 tweet volume'''
import imageio
from wordcloud import WordCloud

df1 = pd.DataFrame(storedTopic,columns=["Tweet", "Volume"])
a = df1["Volume"] > 20000
df2 = df1[a]


text = dict(zip(df2['Tweet'].tolist(), df2['Volume'].tolist()))
maskImage = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask = maskImage, background_color="white")
wordcloud = wordcloud.generate_from_frequencies(text)
wordcloud = wordcloud.to_file("tweet_cloud.png")
plt.imshow(wordcloud)

plt.show()
