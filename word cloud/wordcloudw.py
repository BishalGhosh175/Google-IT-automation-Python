from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud
file = open("mp.txt", "r")
# Read text
text = file.read()
stopwords = STOPWORDS
wc = WordCloud(background_color="white", stopwords=stopwords, height=600, width=400)
wc.generate(text)

# store to file
wc.to_file("wordcloud_output.png")