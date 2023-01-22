delay = int(input())
wither = int(input())
n = int(input())

flowers = [1]
count = 1

for i in range(1, n+1):
    #flow_copy = flowers.copy()
    for j in flowers:
        if (i - j) > 0 and (i - j) % wither == 0:
            count -= 1
            flowers.remove(j)
            print("day of death:" + str(i))
        if (i - j) > 0 and (i - j) >= delay:
            count += 1
            print(" day of birth:" + str(i))
            flowers.append(i)
        
    #flowers = flow_copy
    print("count: " + str(count))
    
print(count)