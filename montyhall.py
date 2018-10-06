import random

i = 0
n=1000

count = [0, 0, 0]
sum = 0

while i < n:
    number = random.randint(0,2)
    sum += number
    count[number] += 1
    i += 1

print(count)
print("Average = " + str(sum/n))
