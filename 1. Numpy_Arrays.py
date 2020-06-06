#!/usr/bin/env python
# coding: utf-8

# In[73]:


#N- Dimensional Array

import numpy as np #import numpy libary

#create an array list
scores = [44.53,34.65,2.6,90.2,87.3]
scores_array = np.array(scores)

print("Array = ",scores_array)
print("Type = ",scores_array.dtype) #.dtype returns the data type of the array


# In[84]:


#Nested lists with equal length will be converted into multi-dimensional array

scores_m = [[34,56,76,34],[23,54,12,11]]
scores_m_array = np.array(scores_m)

print("Array = ",scores_m_array)
print("Dimmension = ",scores_m_array.ndim) #.ndim gives you the dimensions of an array.
print("Rows, Column = ",scores_m_array.shape) #number of rows and columns
print("Type = ",scores_m_array.dtype)


# In[87]:


#more arrays and functions
x = np.zeros(5)
y = np.ones(5)

np.zeros((4,3)) #mention the shape of the area (4 rows  by 3 columns)
np.arange(15) #the array is the number range: 1, 2, 3....14


# In[88]:


np.eye(6)


# In[91]:


#call scores from above in the below scenario.
scores_array

print("A: ",scores_array * scores_array)
print("B: ",scores_array - scores_array)
print("C: ",1/scores_array)
print("D: ",scores_array ** 0.5)

