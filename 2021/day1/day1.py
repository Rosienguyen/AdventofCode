with open('/Users/rosie/Documents/GitHub/AdventofCode/2021/day1/day1.in') as f: 
    data = [int(x) for x in f.read().split('\n')]

# Part 1
# data = [int(x) for x in data]
start = data[0]
count = 0
for depth in data[1:]: 
    if depth - start >0: 
        count += 1
    start = depth
print(count)

# Part 2
count_2 = 0
start = sum(data[:3])
for ind in range(1, len(data)-3): 
    end = sum(data[ind : (ind+3)])
#     print(start, end)
    if end - start >0:
        count_2 += 1
    start = end
print(count_2)