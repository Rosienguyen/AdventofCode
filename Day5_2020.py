#!/usr/bin/env python
# coding: utf-8

# In[1]:


#https://adventofcode.com/2020/day/5
with open ('Day5.txt', 'rt') as f:
    data = f.read().strip()
data = data.split('\n')
# data[:5]    


# ## Part 1

# In[37]:


def find_position(code,  start, end, left, right): 
    for value in code: 
        if value == left: 
            end = (end + start)//2
            final = end
        else: 
            start = (start + end)//2 + 1
            final = start
    return final
            
def find_id(code): 
    rows = code[:7]
    row_final = find_position(rows, 0, 127, 'F', 'B')
    columns = code[7:]
    col_final = find_position(columns, 0, 7, 'L',  'R')
    return (row_final * 8 + col_final)
            
max_id = 0
for seat in data: 
    max_id = max(max_id, find_id(seat))
print(max_id)


# ## Part 2

# In[43]:


seats = set()
for seat in data:
    seats.add(find_id(seat))
all_seats = set()
for i in range(min(seats), max(seats)+1):
    all_seats.add(i)
print(all_seats.difference(seats))


# In[38]:


#Credit to AOC founder, Eric Wastl
r = open('Day5.txt').read().strip('\n')
input = r.splitlines()

#Part 1
seats = [int(x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for x in input]
seats.sort()
print(seats[-1])

#Part 2
for x in range(len(seats)):
    if seats[x+1] - seats[x] != 1:
        print(seats[x] + 1)
        break
    


# In[ ]:




