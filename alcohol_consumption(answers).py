#!/usr/bin/env python
# coding: utf-8

# # Ex - GroupBy

# ### Introduction:
# 
# GroupBy can be summarized as Split-Apply-Combine.
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# Check out this [Diagram](http://i.imgur.com/yjNkiwL.png)  
# ### Step 1. Import the necessary libraries

# In[4]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). 

# In[5]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'


# ### Step 3. Assign it to a variable called drinks.

# In[9]:


drinks = pd.read_csv(url)
drinks.head(5)


# ### Step 4. Which continent drinks more beer on average?

# In[16]:


gb = drinks.groupby('continent').agg({
    'beer_servings': 'mean'
    
})


# In[19]:


gb.sort_values('beer_servings')


# In[20]:


drinks.head(1)


# ### Step 5. For each continent print the statistics for wine consumption.

# In[23]:


gb = drinks.groupby('continent').agg({
    'wine_servings': 'describe'
    
})


# In[24]:


gb


# ### Step 6. Print the mean alcohol consumption per continent for every column

# In[28]:


ac = drinks.groupby('continent').mean()
ac


# ### Step 7. Print the median alcohol consumption per continent for every column

# In[29]:


acmed = drinks.groupby('continent').median()
acmed


# In[31]:


drinks.head(1)


# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# In[32]:


drinks.spirit_servings.describe()


# In[ ]:




