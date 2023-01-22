delay = int(input())
wither = int(input())
n = int(input())


#flower = [3, 4, 5, 6, 6]

count = 1
for i in range(1, n+1):
    if i - delay % delay == 0:
        count += count
        
    if i - wither % delay == 0:
        count -= 1 * (wither - delay)
    

print(count)
'''
flowers = [1]


for i in range(1, n+1):
    #flow_copy = flowers.copy()
    for j in flowers:
        if (i - j) > 0 and (i - j) % wither == 0:
            #count -= 1
            flowers.remove(j)
            #print("day of death:" + str(i))
        if (i - j) > 0 and (i - j) >= delay:
            #count += 1
            #print(" day of birth:" + str(i))
            flowers.append(i)
        
    #flowers = flow_copy
    #print("count: " + str(count))
    
print(len(flowers))

'''