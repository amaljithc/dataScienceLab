#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as nup
array=nup.arange(12).reshape(3,4)
print("Original array")
print(array)
header='col1 col2 col3'
nup.savetxt('exc1.txt',array,fmt="%d",header=header)
print("After loading,the contents of the file:")
result=nup.loadtxt('exc1.txt')
print(result)


# In[ ]:




