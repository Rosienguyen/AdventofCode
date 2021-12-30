#!/usr/bin/env python
# coding: utf-8

# In[156]:


#https://adventofcode.com/2020/day/9
with open ('Day9.txt', 'rt') as f: 
    data = [int(x) for x in  f.read().split('\n')]
data[:5]


# In[159]:


#Part 1
moving = data[:25]
dictionary = {}
position = 24
positions = {}
for pos, number in enumerate(data[25:]):
#     print('search:', number,' in ', moving)
    for ind, preamble in enumerate(moving):
        res = number - preamble
#         print(preamble, res)
        if res in moving[ind+1:]:
            position += 1
#             dictionary[number] = [ preamble, res]
#             print('position ', position, ' of ', number, 'is sum of', (preamble, res))
            moving = moving[1:]
            moving.append(number)
            positions[position] = number
            break
            
    if number != positions.get(pos+25): 
        posi = pos + 25
        odd = data[pos+25]
        print(posi, odd )
        break


# In[161]:


#Part 2
new_data = data[:posi]
for pos, number in enumerate(new_data[:-1]):
    for length in range(2,len(new_data)+1): 
        moving = new_data[pos:length]
        if sum(moving) == odd: 
            print(min(moving) + max(moving))
#             print(moving)
            break


# In[ ]:




