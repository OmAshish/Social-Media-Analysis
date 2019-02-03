
"""
Created on Wed Oct  3 21:44:06 2018

@author: Om
"""
import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im
consumer_key = 'hzNYHN9xRlXeKu7g2aj7nWNAI'
consumer_secret = 'Xm3ScyKHRL5EBXdr08n1IHuJjO3YLv1ea68Td5rVCVo56SsYNq'
twitter = Twython(consumer_key, consumer_secret)
access_key = '78845728-kLsebXB9e0WCdRMxISdaIRbx2pNzgUzsrNSKSbYDy'
access_secret = 'jd7cOjgDi0rysph8kznb4pqofoA0TqFtlUs1RmCJBCPsf'

#Get timeline 
user_timeline=twitter.get_user_timeline(screen_name='depression',count=1) 
#get most recent id
last_id = user_timeline[0]['id']-1
for i in range(16):
    batch = twitter.get_user_timeline(screen_name='depression',count=200, max_id=last_id)
    user_timeline.extend(batch)
    last_id = user_timeline[-1]['id'] - 1
#Extract textfields from tweets
raw_tweets = []
for tweets in user_timeline:
    raw_tweets.append(tweets['text'])
#Create a string form of our list of text
raw_string = ''.join(raw_tweets)
no_links = re.sub(r'http\S+', '', raw_string)
no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
words = no_special_characters.split(" ")
words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
words = [w.lower() for w in words]
words = [w for w in words if w not in STOPWORDS]
wc = WordCloud(background_color="white", max_words=2000, mask=None)
clean_string = ','.join(words)
wc.generate(clean_string)
f = plt.figure(figsize=(30,30))
f.add_subplot(1,2, 1)
#plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.title('Original Stencil', size=40)
#plt.axis("off")
#f.add_subplot(1,2, 2)
plt.imshow(wc, interpolation='bilinear')
plt.title('Twitter Generated Cloud', size=40)
plt.axis("off")
plt.show()