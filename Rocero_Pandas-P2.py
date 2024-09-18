#!/usr/bin/env python
# coding: utf-8

# # Problem 2

# In[2]:


#Import pandas as library
import pandas as pd


# ### Load the corresponding .csv file into a data frame named cars using pandas

# In[3]:


cars = pd.read_csv('cars.csv')


# ### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

# In[4]:


#Print data frame with odd-numbered columns that contains the first five rows
odd = cars.iloc[:5,::2]
odd


# ### Display the row that contains the ‘Model’ of ‘Mazda RX4’.

# In[5]:


#Print the row for the model "Mazda RW4 Wag
cars.loc[[1]] 


# ### How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# In[6]:


#Print the cyl value for car model "Camaro Z28" 
cars.loc[[23],['cyl']]


# ### Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# 

# In[14]:


#Print the cyl and gear of the given model cars
cars.loc[[1,18,28],['Model','cyl','gear']] 


# In[ ]:




