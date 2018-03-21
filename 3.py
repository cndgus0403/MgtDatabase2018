print("Problem 3")

num = 0
for i in range(0,31,2):
    if i%8 == 0:
        continue

    num = num + i
    
print("sum = ",num)
