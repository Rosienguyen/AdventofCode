with open('/Users/rosie/Documents/GitHub/AdventofCode/2021/day2/day2.in') as f: 
    data = f.read().split('\n')

# Part 1
horizon = 0
depth = 0
for command in data:
    com, step = command.split()
    step = int(step)
#     print(com, step)
    if com == 'forward': 
        horizon += step
    if com == 'down': 
        depth += step
    if com == 'up': 
        depth -= step
print(horizon * depth)

# Part 2
horizon = 0
depth = 0
aim = 0
for command in data:
    com, step = command.split()
    step = int(step)
#     print(com, step)
    if com == 'forward': 
        horizon += step
        depth += aim * step
    if com == 'down': 
#         depth += step
        aim += step
    if com == 'up': 
#         depth -= step
        aim -= step
print(horizon * depth)