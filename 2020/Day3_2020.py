#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://adventofcode.com/2020/day/3
file = open('Day3.txt')
data = file.readlines()
# data


# In[2]:


data = [x.strip() for x in data]
# data


# ## Part 1

# In[3]:


def count_trees(right, step, data):
    position = 0
    tree = 0
    for ind in range(0, len(data),step):
        line = data[ind]
        if len(line)-1 < position: 
            line = line *(position//len(line) +1)
        if line[position] == '#':
            tree += 1
        position += right
    return tree
count_trees(3,1,data)    


# ## Part 2

# In[75]:


rights = [1,3,5,7,1]
steps = [1,1,1,1,2]
tree_found = 1
for right, step in zip(rights, steps): 
    tree = count_trees(right, step, data)
    tree_found *= tree
tree_found


# In[ ]:




