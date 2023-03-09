import random

x = int(input("Type the number of attempts: "))

total = 0

count = 0

while count < x:
    count += 1
    result1 = random.randint(1,6)
    result2 = random.randint(1,6)
    result = result1 + result2
    total += result
    average = total / count
    print(average)