#!/usr/bin/env python
# coding: utf-8

# # Day 1

# ## Part 1

# In[3]:


#https://adventofcode.com/2020/day/1
file = open("Day1.txt", 'r')


# In[4]:


data = file.read().strip().splitlines()
data = [int(i) for i in data]
# data


# In[7]:


# Solution 1
for ind, value in enumerate(data): 
    rest = 2020- value
    if rest in data[ind+1: ]: 
        print(value, rest, value * rest)


# In[8]:


# Solution 2
p = {}
for ind, value in enumerate(data): 
    rest = 2020- value
    p[value] = rest
    if value == p.get(rest):
        print(value, rest, value * rest)


# In[9]:


#Solution 3
for i in range(len(data)): 
    for j in range( i+1, len(data)-1): 
        if data[i] + data[j] == 2020: 
            print(data[i], data[j], data[i] *data[j])


# ## Part 2

# In[12]:


# Solution 1
for i in range(len(data)-2): 
    for j in range( i+1, len(data)-1): 
        for k in range(j+1, len(data)): 
            if data[i] + data[j] + data[k] == 2020: 
                print(data[i], data[j], data[k], data[i] *data[j] * data[k])


# In[13]:


# Solution 2
results = {}
for ind, value in enumerate(data[:-3]): 
    rest = 2020- value
    for value2 in data[ind+1:]: 
        rest2= rest - value2
        results[value2] = rest2
        if value2 == results.get(rest2): 
            print(value,rest2, value2,  value *value2* rest2)
            break


# In[ ]:




