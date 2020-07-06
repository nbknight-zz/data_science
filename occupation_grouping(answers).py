#!/usr/bin/env python
# coding: utf-8

# # Occupation

# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[2]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# ### Step 3. Assign it to a variable called users.

# In[6]:


users = pd.read_csv(url,'|')
users


# ### Step 4. Discover what is the mean age per occupation

# In[12]:


us = users.groupby('occupation')
us.age.mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[14]:


users.head()


# In[17]:


def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0
    
users['gender_n'] = users['gender'].apply(gender_to_numeric)

a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100

a.sort_values(ascending = False)


# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[18]:


us.age.describe()


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[19]:


users.head(1)


# In[20]:


users.groupby(['occupation', 'gender']).age.mean()


# ### Step 8.  For each occupation present the percentage of women and men

# In[24]:


# create a data frame and apply count to gender
gender_ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})

# create a DataFrame and apply count for each occupation
occup_count = users.groupby(['occupation']).agg('count')

# divide the gender_ocup per the occup_count and multiply per 100
occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

# present all rows from the 'gender column'
occup_gender.loc[: , 'gender']


# In[ ]:




