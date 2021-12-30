with open('/Users/rosie/Documents/GitHub/AdventofCode/2021/day3/day3.in') as f: 
    data = f.read().split('\n')

# Part 1
result = dict()
for i in data:
    for j in range(12): 
        result[j] = result.get(j,0) + (i[j]=='1')
gamma = list()
epsilon = list()
for key, val in result.items(): 
    if val > len(data)//2: 
        gamma.append("1")
        epsilon.append("0")
    else: 
        gamma.append("0")
        epsilon.append("1")
gamma = "".join(gamma)
epsilon = "".join(epsilon)
print(gamma, epsilon)

# Part 2
def find_most_number(data, gamma):
    lst = data.copy()
    bit = gamma[0]
    for index in range(len(gamma)):
        count = 0
        if len(lst)>1: 
            new_data = []
            for num in lst: 
                if num[index] == bit:
                    new_data.append(num)
                    if index +1 == len(gamma): 
                        continue
                    else: 
                        if num[index +1] == '1': 
                            count +=1
            lst = new_data
            # print(f'The position{index} with {bit} has', len(lst))
            if index + 1 < len(gamma): 
                if count >= len(lst)/2: 
                    bit = '1'
                else: 
                    bit = '0'

        if len(lst)==1: 
            return lst[0]
        
def find_least_number(data, epsilon):
    lst = data.copy()
    bit = epsilon[0]
    for index in range(len(epsilon)):
        count = 0
        if len(lst)>1: 
            new_data = []
            for num in lst: 
                if num[index] == bit:
                    new_data.append(num)
                    if index +1 == len(epsilon): 
                        continue
                    else: 
                        if num[index +1] == '0': 
                            count +=1
            lst = new_data
            # print(f'The position{index} with {bit} has', len(lst))
            if index + 1 < len(epsilon): 
                if count <= len(lst)/2: 
                    bit = '0'
                else: 
                    bit = '1'
        if len(lst)==1: 
            return lst[0]
        
oxygen = find_most_number(data, gamma)
CO2 = find_least_number(data, epsilon)
print(int(oxygen,2) * int(CO2,2))