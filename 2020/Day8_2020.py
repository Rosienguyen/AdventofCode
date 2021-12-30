#!/usr/bin/env python
# coding: utf-8

# In[53]:


#https://adventofcode.com/2020/day/8
with open('Day8.txt', 'rt') as f: 
    data = f.read().split('\n')
data[:5]


# In[54]:


instructions = {}
for ind, instruction in enumerate(data):
    command, step = instruction.split()
    instructions[ind] = [command, int(step)]
# instructions


# In[57]:


def procedure (instructions, key, accumulator):   
    command, step = instructions.get(key)
#     print('key: ', key, ', command:', command)
    if command == 'nop': 
        key += 1
#         print('command : nop',   ', accumulator: ', accumulator)
    elif command == 'jmp':  
        key += step
#         print('command :', command, ', accumulator: ', accumulator)
    else: 
        key += 1
        accumulator += step
#         print('command :', command, ', accumulator: ', accumulator)
    return key, accumulator


# In[66]:


# Part 1

key = 0 
accumulator = 0 
keys = list()

while True: 
    key, accumulator = procedure(instructions, key, accumulator)
    if key not in keys: 
        keys.append(key)
    else: 
        break
accumulator 


# In[67]:


#Part 2

def search_change(k, instructions): 
    dict_change = {'nop': 'jmp', 'jmp': 'nop'}
    instructions_2 = {}
    key_2 = 0
    keys_2 = list()
    accu = 0
    last_key = max(instructions.keys())
    for old_value, new_value in dict_change.items(): 
        if instructions.get(k)[0] == old_value:
            dict_update={k:[new_value,instructions.get(k)[1]]}
            instructions_2.update(instructions)
            instructions_2.update(dict_update)
            while last_key not in keys_2: 
                key_2, accu = procedure(instructions_2, key_2, accu)
                if key_2 not in keys_2: 
                    keys_2.append(key_2)
                else: 
                    break
            if keys_2[-1] == last_key: 
                key_2, accu = procedure(instructions_2, key_2, accu)
                print('final_accumulator:', accu)
                break
#                 return accu

for k in keys:
    search_change(k, instructions)


# In[ ]:




