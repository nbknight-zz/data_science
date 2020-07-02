#!/usr/bin/env python
# coding: utf-8

# # Exercise 1

# ### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-facts/data

# In[5]:


ls


# ### Step 2. Download the dataset to your computer and unzip it.

# In[7]:


import pandas as pd


# ### Step 3. Use the tsv file and assign it to a dataframe called food

# In[11]:


food = pd.read_csv('en.openfoodfacts.org.products.tsv', sep='\t')


# ### Step 4. See the first 5 entries

# In[17]:


pd.set_option('display.max_rows', 200)


# In[18]:


food.head(5).T


# ### Step 5. What is the number of observations in the dataset?

# In[20]:


food.info()


# ### Step 6. What is the number of columns in the dataset?

# In[ ]:





# ### Step 7. Print the name of all the columns.

# In[28]:


for i in food.columns:
    print(i)


# ### Step 8. What is the name of 105th column?

# In[30]:


food.columns[104]


# ### Step 9. What is the type of the observations of the 105th column?

# In[37]:


food[['-glucose_100g']].info()


# ### Step 10. How is the dataset indexed?

# In[42]:


pd.set_option('display.max_colwidth',300)


# In[43]:


food[['code', 'url']]


# ### Step 11. What is the product name of the 19th observation?

# In[46]:


food.at[18, 'product_name']


# In[ ]:




