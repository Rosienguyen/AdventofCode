#!/usr/bin/env python
# coding: utf-8

# In[59]:


#https://adventofcode.com/2020/day/7
with open('Day7.txt', 'rt') as f: 
    data = f.read().strip()
data = data.split('.\n')
len(data)


# In[62]:


# Part 1 - Solution 1
rules = {}
import re
pattern = r'[0-9]'
for rule in data:
    rule = rule.replace(' bags','').replace(' bag','')
    outer_bag, inner_bag = rule.split(' contain ')
    inner_bag = re.sub(pattern, '',inner_bag)
    if inner_bag.strip() == 'no other': 
        pass
    else: 
        rules[outer_bag] = inner_bag.strip().split(',  ')
# rules
def recursive_dfs(graph, source,path = set()):
    for key, value in graph.items(): 
        if source in value:
#             print('value:',value, 'key:', key )
            path.add(key)
            if recursive_dfs(graph, key, path) is None: 
                path.add(i for i in recursive_dfs(graph, key, path))
    return path

outer_bags = recursive_dfs(rules, "shiny gold")

len(outer_bags)


# In[1]:


#Part 1 - Solution 2
with open("Day7.txt", "rt") as f:
    data = f.read()
data = data.strip().split("\n")
bagspecs = []
for bag in data:
    bag = bag.replace(" bags", "").replace(" bag", "")
    name, contents = bag.split(" contain ")
    assert contents.endswith(".")
    contents = contents[:-1]
    inner_bags = []
    if contents == "no other":
        continue
    for count_bagtype in contents.split(", "):
        count, bagtype = count_bagtype.split(" ", 1)
        inner_bags.append((int(count), bagtype))
    bagspecs.append((name, inner_bags))

import collections
edges = collections.defaultdict(list)
for name, inner_bags in bagspecs:
    for _, innername in inner_bags:
        edges[innername].append(name)

visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for child in edges[node]:
#         print('parents: ', node, ', child: ', child)
        dfs(child)
    return visited

print(len(dfs("shiny gold"))-1)


# In[5]:


#Part 2

edges = dict(bagspecs)

visited = set()

def num_visited(node): # node = green
    res = 1
#     print('parent_node:', node)
    for count, child in edges.get(node, []):
        
        magic = num_visited(child) # num_visited = 2
#         print('node:', node, ', res: ', res, ', count: ', count, ', child: ', child, ', magic: ', magic)
        res += count * magic
#         print('res_total: ', res)
    return res
print(num_visited("shiny gold") - 1)
# print(num_visited("red") - 1)


# In[ ]:




