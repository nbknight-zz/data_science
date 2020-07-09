#!/usr/bin/env python
# coding: utf-8

# # MPG Cars

# ### Introduction:
# 
# The following exercise utilizes data from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Auto+MPG)
# 
# ### Step 1. Import the necessary libraries

# In[28]:


import pandas as pd
import numpy as np


# ### Step 2. Import the first dataset [cars1](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv) and [cars2](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv).  

# In[2]:


ls


#    ### Step 3. Assign each to a variable called cars1 and cars2

# In[3]:


cars1 = pd.read_csv('cars1.csv')


# In[4]:


cars2 = pd.read_csv('cars2.csv')


# In[16]:


cars1.head()


# In[6]:


cars2.head()


# ### Step 4. Oops, it seems our first dataset has some unnamed blank columns, fix cars1

# In[18]:


cars1.drop(columns=['Unnamed: 9', 'Unnamed: 10',
       'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'], inplace=True)


# In[19]:


cars1.columns


# In[20]:


cars1.head()


# ### Step 5. What is the number of observations in each dataset?

# In[22]:


cars1.info()
cars2.info()


# ### Step 6. Join cars1 and cars2 into a single DataFrame called cars

# In[23]:


assert all(cars1.columns == cars2.columns)


# In[27]:


cars = pd.concat([cars1,cars2], axis=0)
cars.shape


# ### Step 7. Oops, there is a column missing, called owners. Create a random number Series from 15,000 to 73,000.

# In[29]:


owners = np.random.randint(15000,73001, size=398)
len(owners)


# In[ ]:





# ### Step 8. Add the column owners to cars

# In[30]:


cars['ownsers'] = owners
cars.head()


# In[ ]:




