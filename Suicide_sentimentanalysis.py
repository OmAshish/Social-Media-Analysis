# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:47:19 2018

@author: OM
"""
import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
#Does plotting as well as analysis
consumer_key='hzNYHN9xRlXeKu7g2aj7nWNAI'
consumer_secret='Xm3ScyKHRL5EBXdr08n1IHuJjO3YLv1ea68Td5rVCVo56SsYNq'

access_token_key='78845728-kLsebXB9e0WCdRMxISdaIRbx2pNzgUzsrNSKSbYDy'
access_token_secret='jd7cOjgDi0rysph8kznb4pqofoA0TqFtlUs1RmCJBCPsf'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)

topicname=input("Enter the topic you want to search about\n")
number=int(input("Enter the number of tweets to search\n"))
public_tweets=api.search( 
   lang="en",
   q=topicname + " -rt",
   count=number, result_type='mixed')

unwanted_words=['@','RT',':','https','http']
symbols=['@','#']
data=[]
data = pd.DataFrame(data=[tweet.text for tweet in public_tweets], columns=['Tweets'])
display(data.head(number))
data['len']  = np.array([len(tweet.text) for tweet in public_tweets])
data['ID']   = np.array([tweet.id for tweet in public_tweets])
data['Date'] = np.array([tweet.created_at for tweet in public_tweets])
data['Source'] = np.array([tweet.source for tweet in public_tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in public_tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in public_tweets])
display(data.head(number))
fav_max = np.max(data['Likes'])
rt_max  = np.max(data['RTs'])

fav = data[data.Likes == fav_max].index[0]
rt  = data[data.RTs == rt_max].index[0]

# Max FAVs:
print("The tweet with most likes is: \n{}".format(data['Tweets'][fav]))
print("Number of likes: {}".format(fav_max))
print("{} characters.\n".format(data['len'][fav]))

# Max RTs:
print("The tweet with most retweets is: \n{}".format(data['Tweets'][rt]))
print("Number of retweets: {}".format(rt_max))
print("{} characters.\n".format(data['len'][rt]))
tlen = pd.Series(data=data['len'].values, index=data['Date'])
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])
tlen.plot(figsize=(16,4), color='r');
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True); 
plt.show()
countpos=countneg=countneut=0
arr=[]
a1=[]
for tweet in public_tweets:
    tweeta = tweet.text
    tidy_tweet = (tweeta.strip().encode('ascii', 'ignore')).decode("utf-8") 
    
    analysis= TextBlob(tidy_tweet)
    #print (analysis.sentiment)
    if(analysis.sentiment.polarity > 0.2):
        polarity = 'Positive'
        countpos=countpos+1
        pol=1
    elif(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
        countneut=countneut+1
        pol=0
    elif(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
        countneg=countneg+1
        pol=-1
        
    #dic={}
    arr.append(polarity)
    a1.append(pol)
    
se=pd.Series(arr)
df=pd.DataFrame(data)
df['Sentiment']=se.values
ss=pd.Series(a1)
df['Senti']=ss.values
#print(df)

df.to_csv('analysedfile.csv')
positive = countpos
negative = countneg
neutral = countneut
colors = ['blue', 'red', 'yellow']
sizes = [positive, negative, neutral]
labels = 'Positive', 'Negative', 'Neutral'
plt.pie(
   x=sizes,
   shadow=True,
   colors=colors,
   labels=labels,
   startangle=90
)

plt.title("Sentiment of {} Tweets about {}".format(number, topicname))
plt.show()
percpos=(countpos/int(number))*100
percneg=(countneg/int(number))*100
percneut=(countneut/int(number))*100
print("\nPercentage of positive tweets:",percpos)
print("\nPercentage of negative tweets:",percneg)
print("\nPercentage of neutral tweets:",percneut)