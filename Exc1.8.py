#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as nup
x=nup.array([[10,20,30],[20,30,40],[30,50,60]])
y=nup.array([[10,20,30],[20,30,40],[30,50,60]])
z=nup.array([[10,40,30],[10,30,40],[30,60,70]])
print("To check the arrays x,y are equal or not")
print(nup.equal(x,y))
print("To check the arrays x,z are equal or not")
print(nup.equal(x,z))


# In[ ]:




