#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://adventofcode.com/2020/day/6
with open ('Day6.txt', 'rt') as f: 
    data = f.read().strip()
data = data.split('\n\n')
# data[:5]


# In[64]:


# part 1
total_yes = 0
remove = set(['\n'])
for group in data:
    yes_answers = list(set(group).difference(remove))
    total_yes += len(yes_answers)
print(total_yes)


# In[92]:


#part 2
common_yes = 0
for group in data:
    for ind, traveler in enumerate(group.split()):
#         print('set',set(traveler))
        if ind == 0: 
            yes_answers = set(traveler)
        yes_answers = yes_answers.intersection(set(traveler))
    common_yes += len(yes_answers)
print(common_yes)    
  


# In[93]:


# Credit to Eric Wastl
r = open('Day6.txt').read().strip('\n')
input = r.split('\n\n')

#Part 1:
count = 0
for group in input:
    for question in 'qwertyuiopasdfghjklzxcvbnm':
        if question in group:
            count = count + 1
print(count)

#Part 2:
count = 0
for group in input:
    group = group.splitlines()
    ans = set(group[0])
    for person in group:
        ans = ans & set(person)
    count = count + len(ans)

print(count)


# In[ ]:




