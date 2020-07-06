#!/usr/bin/env python
# coding: utf-8

# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# In[2]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'


# ### Step 3. Assign it to a variable called chipo.

# In[3]:


chipo = pd.read_csv(url,sep='\t')


# In[4]:


chipo.head()


# ### Step 4. How many products cost more than $10.00?

# In[5]:


chipo.info()
##item_price is a string


# In[6]:


get_ipython().run_line_magic('pinfo', 'pd.to_numeric')


# In[7]:


chipo['price_float'] = pd.to_numeric(chipo.item_price.str.slice(1))


# In[8]:


chipo['price_float'].head()


# In[9]:


(chipo['price_float'] > 10).sum()


# In[ ]:





# In[14]:


chipo['price_per_item'] = chipo.price_float / chipo.quantity


# In[15]:


product_prices = chipo.groupby('item_name').agg({'price_per_item':'max'})


# In[42]:


product_prices.info()


# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# In[16]:


(product_prices.price_per_item > 10).sum()


# In[17]:


product_prices


# In[ ]:





# ### Step 6. Sort by the name of the item

# In[19]:


product_prices.sort_index()


# ### Step 7. What was the quantity of the most expensive item ordered?

# In[20]:


chipo.head()


# In[22]:


chipo.price_float.idxmax()


# In[23]:


chipo.loc[3598, :]


# ### Step 8. How many times was a Veggie Salad Bowl ordered?

# In[27]:


chipo[chipo.item_name == 'Veggie Salad Bowl'].quantity.sum()


# ### Step 9. How many times did someone order more than one Canned Soda?

# In[29]:


(chipo[chipo.item_name == 'Canned Soda'].quantity > 1).sum()


# In[ ]:




