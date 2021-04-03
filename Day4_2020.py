#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://adventofcode.com/2020/day/4
file = open('Day4.txt')
data = file.readlines()
# data.append('\n')
data = [line.strip() for line in data]
# data


# ## Part 1

# In[13]:


# Solution 1
with open ('Day4.txt', 'rt') as f: 
    data = f.read().strip()
# data
passports = data.split("\n\n")

# using "\n\n" to split into each passport
REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
num_valid = 0
for passport in passports:
    found_fields = set()
    #make sure that the list is not duplicated
    for kv in passport.split(): 
        # a way to split each field. with split(), it takes any whitespace including (\n) as delimiter
        k = kv.split(":")[0] #take the first part of the split
        found_fields.add(k)
#     print(found_fields)
    if REQUIRED_FIELDS.difference(found_fields) == set(): 
        num_valid += 1
print(num_valid)
        


# In[2]:


# Solution 2
import re
valid = 0
traveler = []
travelers = []
for line in data:
    if line == '':
        if traveler is None: 
            pass
        travelers.append(traveler)
        traveler = []
    else: 
        for field in re.split(':| ', line): 
            traveler.append(field)
travelers.append(traveler)
valid = 0
for passport in travelers: 
     if len(passport) == 16 or (len(passport) == 14 and 'cid' not in passport):
            valid += 1
valid            


# ## Part 2

# In[3]:


# Solution 1
def byr(byr):
    return (len(byr) ==4 and  1920 <= int(byr)  <= 2002)

def iyr(iyr): 
    return (len(iyr) == 4 and 2010 <= int(iyr) <= 2020)

def eyr(eyr): 
    return (len(eyr)== 4 and 2020 <= int(eyr) <= 2030)

def hgt(hgt):
    if hgt[-2:] == 'cm': 
        return ( 150<= int(hgt[:-2])<= 193)
    elif hgt[-2:] =='in': 
        return (59 <= int(hgt[:-2])<= 76)
    return False

def ecl(ecl): 
    eyes= ['amb',  'blu',  'brn',  'gry',  'grn',  'hzl',  'oth']
    return (ecl in  eyes)

def hcl(hcl): 
    target = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    total = 0
    if  (hcl[0] =='#' and len(hcl[1:]) == 6): 
        for value in hcl[1:]: 
            total += value in target
        if total == 6: 
            return True
    return False

def pid(pid): 
    target = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    total = 0
    if len(pid) == 9: 
        for value in pid: 
            total += value in target
        if total == 9: 
            return True
    return False

total_valid = 0
for traveler in travelers: 
    if len(traveler) == 16 or (len(traveler) == 14 and 'cid' not in traveler):
        valid = 0
        for ind in range(0,len(traveler),2):
            field = traveler[ind]
            if field == 'pid': 
#                 print('pid',traveler[ind+1], pid(traveler[ind+1]))
                valid += pid(traveler[ind+1])
            elif field == 'byr': 
                valid += byr(traveler[ind+1])
#                 print('byr',traveler[ind+1], byr(traveler[ind+1]))
            elif field == 'iyr': 
                valid += iyr(traveler[ind+1])
            elif field == 'hgt': 
                valid += hgt(traveler[ind+1])
#                 print('hgt', traveler[ind+1], hgt(traveler[ind+1]))
            elif field == 'hcl': 
                valid += hcl(traveler[ind+1])
#                 print('hcl', traveler[ind+1], hcl(traveler[ind+1]))
            elif field == 'ecl': 
                valid += ecl(traveler[ind+1])
#                 print('ecl', traveler[ind+1], ecl(traveler[ind+1]))
            elif field  == 'eyr': 
#                 print('eyr', traveler[ind+1], eyr(traveler[ind+1]) )
                valid += eyr(traveler[ind+1])
        total_valid += (valid == 7)
    
total_valid        


# In[15]:


# Solution 2
def valid_height(v):
    if v.endswith('cm'):
        v = v[:-2]
        return isint(v) and 150 <= int(v) <= 193
    elif v.endswith('in'):
        v = v[:-2]
        return isint(v) and 59 <= int(v) <= 76
    else:
        return False


def valid_hair_color(v):
    if not v.startswith('#'):
        return False
    v = v[1:]
    return all(l in '0123456789abcdef' for l in v)


REQUIRED_FIELDS = {
    'byr': lambda v: isint(v) and 1920 <= int(v) <= 2002,
    'iyr': lambda v: isint(v) and 2010 <= int(v) <= 2020,
    'eyr': lambda v: isint(v) and 2020 <= int(v) <= 2030,
    'hgt': valid_height,
    'hcl': valid_hair_color,
    'ecl': lambda v: v in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': lambda v: len(v) == 9 and v.isdigit(),
}


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

with open("Day4.txt", "rt") as f:
    data = f.read().strip()
passports = data.split("\n\n")

num_valid = 0
for passport in passports:
    found_fields = set()
    for kv in passport.split():
        k, v = kv.split(":")
        if k in REQUIRED_FIELDS and REQUIRED_FIELDS[k](v):
            found_fields.add(k)
    if set(REQUIRED_FIELDS).difference(found_fields) == set():
        num_valid += 1
print(num_valid)


# In[ ]:




