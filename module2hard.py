import random

num = random.randint(3, 20)
result = []

for i in range(num):
    
    for j in range(i + 1, num):
        if num % (j + i) == 0 and i != 0 and j != 0:
            result.append(i)
            result.append(j)

print(num, '-', result)
