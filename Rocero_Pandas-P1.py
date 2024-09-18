#!/usr/bin/env python
# coding: utf-8

# # Problem 1

# In[1]:


#Import pandas as library
import pandas as pd


# ### Load the corresponding .csv file into a data frame named cars using pandas

# In[2]:


#Input the cars.csv file
cars = pd.read_csv('cars.csv')
cars


#  ### Print the first and last five rows of the resulting cars

# In[3]:


#Print first 5 rows 
cars.head() 


# In[4]:


#print last 5 rows
cars.tail() 


# In[ ]:




