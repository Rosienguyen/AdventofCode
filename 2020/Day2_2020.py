#!/usr/bin/env python
# coding: utf-8

# # Day 2

# ## Part 1

# In[1]:


#https://adventofcode.com/2020/day/2
file = open("Day2.txt")
data = file.readlines()
data = [s.strip() for s in data]
# data


# In[72]:


valid = 0 
for element in data: 
    value, chars = element.split(': ')
    start_end, letter = value.split(' ')
    start, end = map(int, start_end.split('-'))
    count = 0
    for let in chars: 
        if let == letter: 
            count += 1
    if count >= start and count <= end:
        valid += 1
valid


# ## Part 2

# In[71]:


valid = 0 
for element in data: 
    value, chars = element.split(': ')
    start_end, letter = value.split(' ')
    start, end = start_end.split('-')
    if (chars[int(start)-1] == letter and chars[int(end)-1] != letter) or (chars[int(start)-1] != letter and chars[int(end)-1] == letter):
        valid += 1
valid

