#!/usr/bin/env python
# coding: utf-8

# # Ex2 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# In[3]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'


# In[4]:


df = pd.read_csv(url, '\t')


# ### Step 3. Assign it to a variable called chipo.

# In[5]:


chipo = df


# ### Step 4. See the first 10 entries

# In[6]:


chipo.head(10)


# ### Step 5. What is the number of observations in the dataset?

# In[7]:


# Solution 1
chipo.info()


# In[8]:


# Solution 2

chipo.shape


# ### Step 6. What is the number of columns in the dataset?

# In[9]:


chipo.shape


# ### Step 7. Print the name of all the columns.

# In[10]:


chipo.columns


# ### Step 8. How is the dataset indexed?

# In[11]:


chipo.index


# ### Step 9. Which was the most-ordered item? 

# In[12]:


item_quants = chipo.groupby(['item_name']).agg({'quantity': 'sum'})
item_quants.sort_values('quantity', ascending=False)[:1]


# ### Step 10. For the most-ordered item, how many items were ordered?

# In[13]:


item_quants = chipo.groupby(['item_name']).agg({'quantity': 'sum'})
item_quants.sort_values('quantity', ascending=False)[:1]


# ### Step 11. What was the most ordered item in the choice_description column?

# In[14]:


item_quants = chipo.groupby(['choice_description']).agg({'quantity': 'sum'})
item_quants.sort_values('quantity', ascending=False)[:1]


# ### Step 12. How many items were orderd in total?

# In[15]:


chipo.quantity.sum()


# ### Step 13. Turn the item price into a float

# #### Step 13.a. Check the item price type

# In[17]:


chipo['item_price'] = chipo.item_price.str.slice(1).astype(float)


# In[22]:


chipo.info()


# In[23]:


pd.to_numeric


# #### Step 13.b. Create a lambda function and change the type of item price

# In[18]:


lam = lambda x: str(x[1:])
chipo.item_price.apply(lam)


# #### Step 13.c. Check the item price type

# In[21]:


chipo['item_price'].sum()


# ### Step 14. How much was the revenue for the period in the dataset?

# In[20]:


chipo.head(10)


# In[23]:


chipo['item_price'].sum()


# ### Step 15. How many orders were made in the period?

# In[24]:


chipo['quantity'].sum()


# ### Step 16. What is the average revenue amount per order?

# In[38]:


# Solution 1
chipo['item_price'].sum() / chipo.shape[:1]


# In[39]:


# Solution 2
chipo['item_price'].mean()


# ### Step 17. How many different items are sold?

# In[44]:


chipo.item_name.nunique()


# In[ ]:




