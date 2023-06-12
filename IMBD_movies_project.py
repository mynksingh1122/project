#!/usr/bin/env python
# coding: utf-8

# # project 3- movies

# In[161]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("movies.csv")#import data from file
print(data)
print(data.info())
print(data.describe())#This function help us to describe the arithamtic operation to understand the data


# In[162]:


#This function show the starting values of head of sheet
df = data.head(20)
print(df)


# In[163]:


#This function help us to find the sum of null values
print(data.isnull().sum())


# In[164]:


#group by on the basis of movie_id to find genre group
gp=df.groupby("genre").agg({"movie_id":"count"})
print(gp)


# In[191]:


# plot a graph to show the distribution of genre in the top 250 movies 

exp=[0,0,0,0,0,0,0,0,0,0.2,0,0,0]
plt.pie(gp["movie_id"],labels=gp.index,autopct="%1.0f%%",labeldistance=1,pctdistance=0.8,shadow="true",
        startangle=210,counterclock="true",explode=exp)
plt.title("Distribution of genre on 20 movies in %",color="Green", loc = "center")
plt.legend(bbox_to_anchor = (1.5,1.1))

plt.show()


# In[166]:


#Another method for finding count of "genre"

sns.countplot(data=pie, x= "genre")
plt.xticks(rotation=40,ha="right",)
plt.show()


# In[175]:


#maximum number of votes of movies 

df["imbd_votes"]==df["imbd_votes"].str.replace(",","").astype(int)
data=(df["imbd_votes"].max())
print(data)



# In[199]:


# which genre it belongs to and its duration with movie name
maximum = df[df['imbd_votes'] == df['imbd_votes'].max()]
print("Movie:", maximum['title'].values[0])
print("Genre:", maximum['genre'].values[0])
print("Duration:", maximum['duration'].values[0])


# In[180]:


#minimum number of votes of movies

df["imbd_votes"]==df["imbd_votes"].str.replace(",","").astype(int)
data =(df["imbd_votes"].min())
print(data)


# In[198]:


# which genre it belongs to and its duration with movie name

minimum = df[df['imbd_votes'] == df['imbd_votes'].min()]
print("Movie:", minimum['title'].values[0])
print("Genre:", minimum['genre'].values[0])
print("Duration:", minimum['duration'].values[0])



# In[46]:


# movies of each genre which has maximum number of votes. 

max_vote=pie.groupby("genre").agg({"imbd_votes":"max"})
print(max_vote)
# max_voted_movies=pie["imbd_votes"].isin(max_vote["imbd_votes"]).loc[["title","genre","imbd_votes"]]
# print(max_voted_movies)

