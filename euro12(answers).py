#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv). 

# In[2]:


ls


# In[4]:


df = pd.read_csv('Euro_2012_stats_TEAM.csv')


# ### Step 3. Assign it to a variable called euro12.

# In[6]:


euro12 = df


# ### Step 4. Select only the Goal column.

# In[8]:


euro12.head()


# In[10]:


euro12.Goals


# ### Step 5. How many team participated in the Euro2012?

# In[11]:


euro12.Team.count()


# In[ ]:





# ### Step 6. What is the number of columns in the dataset?

# In[16]:


euro12.shape


# ### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline

# In[19]:


discipline = euro12[['Team','Yellow Cards','Red Cards']]
discipline


# ### Step 8. Sort the teams by Red Cards, then to Yellow Cards

# In[22]:


discipline.sort_values(['Red Cards','Yellow Cards'], ascending=False)


# ### Step 9. Calculate the mean Yellow Cards given per Team

# In[23]:


discipline['Yellow Cards'].mean()


# ### Step 10. Filter teams that scored more than 6 goals

# In[25]:


euro12.head(1)


# In[31]:


euro12[euro12.Goals > 6]


# ### Step 11. Select the teams that start with G

# In[37]:


euro12[euro12.Team.str.startswith('G')]


# ### Step 12. Select the first 7 columns

# In[40]:


euro12.iloc[:, :7]


# ### Step 13. Select all columns except the last 3.

# In[42]:


euro12.iloc[:, :-3]


# In[ ]:





# ### Step 14. Present only the Shooting Accuracy from England, Italy and Russia

# In[44]:


euro12.set_index('Team', inplace=True)


# In[49]:


euro12.loc[['England', 'Italy', 'Russia'], 'Shooting Accuracy']


# In[ ]:




