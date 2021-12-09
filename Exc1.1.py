#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as nup
x=nup.array([[7,3,2],[1,2,13]])
y=nup.array([[6,7,2],[1,8,9]])
print("original numbers")
print(x)
print(y)
print("Comparison-Greater")
print(nup.greater(x,y))
print("Comparison_Greater--equal")
print(nup.greater_equal(x,y))
print("Comarison--less")
print(nup.less(x,y))
print("COmparison--lese_equal")
print(nup.less_equal(x,y))


# In[ ]:




