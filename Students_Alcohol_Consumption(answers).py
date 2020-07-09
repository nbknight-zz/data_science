#!/usr/bin/env python
# coding: utf-8

# # Student Alcohol Consumption

# ### Introduction:
# 
# This time you will download a dataset from the UCI.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv).

# In[2]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'


# ### Step 3. Assign it to a variable called df.

# In[4]:


df = pd.read_csv(url)


# In[5]:


df.head()


# ### Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column

# In[17]:


slic = df.loc[:,'school':'guardian']


# In[18]:


slic.head()


# ### Step 5. Create a lambda function that will capitalize strings.

# In[19]:


capitalizer = lambda x: x.capitalize()


# ### Step 6. Capitalize both Mjob and Fjob

# In[10]:


slic['Mjob'].apply(capitalizer)
slic['Fjob'].apply(capitalizer)


# ### Step 7. Print the last elements of the data set.

# In[15]:


slic.tail()


# ### Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.

# In[20]:


slic['Mjob'] = slic['Mjob'].apply(capitalizer)
slic['Fjob'] = slic['Fjob'].apply(capitalizer)
slic.tail()


# ### Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)

# In[21]:


def majority(x):
    if x > 17:
        return True
    else:
        return False


# In[22]:


slic['legal_drinker'] = slic['age'].apply(majority)
slic.head()


# ### Step 10. Multiply every number of the dataset by 10. 
# ##### I know this makes no sense, don't forget it is just an exercise

# In[23]:


slic.info()


# In[24]:


def noSense(x):
    if type(x) is int:
        return 10 * x
    return x


# In[25]:


slic.applymap(noSense).head(20)


# In[ ]:




