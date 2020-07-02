#!/usr/bin/env python
# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[2]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# In[3]:


df = pd.read_csv(url, sep='|')


# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[7]:


users = df
users.set_index('user_id', inplace=True) ##this would need to exist


# ### Step 4. See the first 25 entries

# In[9]:


users.head(25)


# ### Step 5. See the last 10 entries

# In[10]:


users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[12]:


users.info() ##943


# ### Step 7. What is the number of columns in the dataset?

# In[21]:


users.info()


# 
# ### Step 8. Print the name of all the columns.

# In[24]:


users.columns


# ### Step 9. How is the dataset indexed?

# In[26]:


users.index.name


# ### Step 10. What is the data type of each column?

# In[27]:


users.info()


# ### Step 11. Print only the occupation column

# In[28]:


users.occupation.head()


# ### Step 12. How many different occupations are in this dataset?

# In[30]:


users.occupation.nunique()


# ### Step 13. What is the most frequent occupation?

# In[33]:


users.head(1)


# In[53]:


users.occupation.value_counts()


# ### Step 14. Summarize the DataFrame.

# In[61]:


users.describe(include='all')


# ### Step 15. Summarize all the columns

# In[66]:





# ### Step 16. Summarize only the occupation column

# In[ ]:





# ### Step 17. What is the mean age of users?

# In[67]:


users.age.mean()


# ### Step 18. What is the age with least occurrence?

# In[68]:


users.age.value_counts(ascending=True)


# In[71]:


pd.cut(users.age, 10).value_counts(ascending=True)[:5]


# In[ ]:




