from pathlib import Path
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt



text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask =mask_image, background_color = "white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoJulietHeart.png")

plt.imshow(wordcloud)
plt.show()
print("done")