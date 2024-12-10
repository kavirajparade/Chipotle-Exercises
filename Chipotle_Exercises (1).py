#!/usr/bin/env python
# coding: utf-8

# # Ex1 - Filtering and Sorting Data

# ### Step 1. Import the necessary libraries

# In[33]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# In[34]:


df = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep="\t")
df


# ### Step 3. Assign it to a variable called chipo.

# In[35]:


chipo = df
chipo


# ### Step 4. How many products cost more than $10.00?

# In[36]:


chipo['item_price'] = chipo['item_price'].str.replace('$','')
chipo['item_price'] = chipo['item_price'].astype(float)
chipo[chipo['item_price']>10.00].shape[0]


# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# In[37]:


chipo[['item_name', 'item_price']]


# ### Step 6. Sort by the name of the item

# In[11]:


chipo.sort_values(by='item_name')


# ### Step 7. What was the quantity of the most expensive item ordered?

# In[7]:


expensive=chipo['item_price'].max()
chipo[chipo['item_price']==expensive]['quantity']


# ### Step 8. How many times was a Veggie Salad Bowl ordered?

# In[13]:


chipo[chipo['item_name']=='Veggie Salad Bowl']['item_name'].count()


# ### Step 9. How many times did someone order more than one Canned Soda?

# In[14]:


sum(chipo[chipo['item_name']=='Canned Soda']['quantity'] > 1)


# ### Step 10. What is the order id of order with the highest total price of all items ordered in that order?

# In[8]:


sum(chipo[chipo['item_price']==chipo['item_price'].max()]['order_id'])


# ### Step 11. In How many orders, atleast one items is ordered multiple times?

# In[20]:


chipo[chipo['quantity']>1].shape[0]


# ### Step 12. Create a billing report (dataframe) which has columns as 'Order_Id', 'Total_Bill', 'Total Bill After Discount'. Restaurant owner has decided to give discount of 5% on orders of above $50 total cost.

# In[17]:


chipo = df.nunique()
chipo


# In[38]:


chipo['Total_Price'] = chipo['quantity'] * chipo['item_price']
total_bill_df = chipo.groupby('order_id')['Total_Price'].sum().reset_index()
total_bill_df.columns = ['Order_Id', 'Total_Bill']

# Apply discount for orders above $50
total_bill_df['Total Bill After Discount'] = total_bill_df['Total_Bill'].apply(
    lambda x: x * 0.95 if x > 50 else x
)

# Display the final billing report
billing_report = total_bill_df
print(billing_report)


# In[ ]:




