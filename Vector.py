#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as n


# In[10]:


import math


# In[11]:


def mag(vec):
    x = vec[0]
    y = vec[1]
    
    return math.sqrt(x**2 + y**2)


# In[ ]:


print(mag([3,5]))


# In[12]:


def unit(vec):
    x = vec[0]
    y = vec[1]
    
    m = mag(vec)
    
    return [x/m,y/m]


# In[ ]:


print(unit([3,5]))


# In[16]:


def rot90(vec):
    x = vec[0]
    y = vec[1]
    
    return n.array([-y,x])


# In[17]:


print(rot90([3,2]))


# In[18]:


a = n.array([3,2])
b = n.array([8,7])
c = n.array([1,5])


# In[19]:


print(2*a)


# In[21]:


print(a+b-c)


# In[24]:


print(n.dot(a,a))
print(mag(a)*mag(a))
print(n.dot(a,b))
print(mag(a)*mag(b))


# In[25]:


a90 = rot90(a)


# In[26]:


print(n.dot(a,a90))


# In[ ]:




