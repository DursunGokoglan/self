import random

x = int(input("Type the number of attempts: "))

total = 0

count = 0

while count < x:
    count += 1
    result = random.randint(0,1)
    total += result
    average = total / count
    print(average)