#!/usr/bin/env python
# coding: utf-8

# In[12]:


# step 1 importing and libraries for calculation and storing data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# stept 2 importing amazon alexa dataset and display first  five recors
df_reviews=pd.read_csv('amazon_alexa.tsv', sep='\t')


# In[3]:


#step 3 display top records
df_reviews.head()


# In[4]:


# step 4 display no of rows and column
df_reviews.shape


# In[5]:


# step 5 display structure of file
df_reviews.info()


# In[6]:


#6 describing descriptive analytics
df_reviews.describe()


# In[7]:


#7 converting data from object to data datatype and displaying year
df_reviews['date']=pd.to_datetime(df_reviews['date'])


# In[8]:


#display year
df_reviews['date'].dt.year.value_counts()


# In[9]:


# displaying minimum date
df_reviews['date'].min()


# In[10]:


#10 displaying maximum date
df_reviews['date'].max()


# In[13]:


#11 displaying data graphically
plt.figure(figsize=(15,16))
sns.countplot(x='date',data=df_reviews)
plt.xticks(rotation=90)
plt.show();


# In[14]:


# 12 displaying three month sales
sns.countplot(df_reviews['date'].dt.month)


# In[15]:


#13 displaying three month sales in numbers
df_reviews['date'].dt.month.value_counts()


# In[16]:


#14 graphical display of user rating
sns.countplot(x='rating',data=df_reviews)


# In[17]:


#15 display numerical alues
df_reviews.rating.value_counts()


# In[18]:


#16 display graph and numerical values of user feedback for amazon alexa products
sns.countplot(x='feedback',data=df_reviews)
df_reviews.feedback.value_counts()


# In[19]:


#step 17 lenghth of review in number and graphs
df_reviews['length']=df_reviews['verified_reviews'].apply(lambda x:len(x.split()))
df_reviews.head()
plt.hist(x='length', data=df_reviews,bins=30)
df_reviews.length.describe()


# In[20]:


pip install wordcloud


# In[22]:


#step 18 generating wordcloud
neg=df_reviews[df_reviews['feedback']==0]
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
text=neg['verified_reviews'].values
wordcloud=WordCloud(
     width=3000,
     height=2000,
     background_color='black',
     stopwords = STOPWORDS).generate(str(text))
fig=plt.figure(
    figsize=(40,30),
    facecolor='k',
    edgecolor='k')
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.tick_params(axis='both',labelsize=14)
plt.show()


# In[23]:


df_reviews['variation'].value_counts().plot.bar()


# In[24]:


df_reviews['variation'].value_counts()


# In[26]:


sns.countplot(x='variation',data=df_reviews)
plt.title('Variation Distribution in Alexa')
plt.xlabel('Variations')
plt.ylabel('count')
plt.xticks(rotation='vertical')
plt.show()


# In[ ]:




