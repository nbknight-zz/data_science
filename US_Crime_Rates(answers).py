#!/usr/bin/env python
# coding: utf-8

# # United States - Crime Rates - 1960 - 2014

# ### Introduction:
# 
# This time you will create a data 
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv). 

# In[2]:


url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'


# In[4]:


df = pd.read_csv(url)


# ### Step 3. Assign it to a variable called crime.

# In[5]:


crime = df
crime.head()


# ### Step 4. What is the type of the columns?

# In[6]:


crime.info()


# ##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
# 
# ### Step 5. Convert the type of the column Year to datetime64

# In[10]:


crime['dt)Year'] = pd.to_datetime(crime.Year, format='%Y')


# In[11]:


crime.head()


# ### Step 6. Set the Year column as the index of the dataframe

# In[15]:


crime.set_index('dt)Year', inplace=True)


# ### Step 7. Delete the Total column

# In[16]:


del crime['Total']


# ### Step 8. Group the year by decades and sum the values
# 
# #### Pay attention to the Population column number, summing this column is a mistake

# In[17]:


crime.head(1)


# In[21]:


crime['Decade'] = crime.Year // 10


# In[22]:


cs = crime.loc[:,'Population': 'Vehicle_Theft'].columns


# In[25]:


agg = {c: 'sum' for c in cs}
agg['Population'] = 'last'
agg['Year'] = 'size'


# In[27]:


gb = crime.groupby('Decade').agg(agg)


# In[18]:


x = pd.to_datetime(crime.Year, format='%Y')


# In[20]:


x.dt.year // 10


# ### Step 9. What is the most dangerous decade to live in the US?

# In[42]:


trends = gb.loc[:,'Violent':'Vehicle_Theft'].div(gb.Year * gb.Population, axis=0)


# In[43]:


trends.plot()


# In[ ]:




