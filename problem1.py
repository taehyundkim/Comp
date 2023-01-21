import math

lst_creeper = input().split(" ")

gcf = int(lst_creeper[0])
for i in range(0, len(lst_creeper) - 1):
    gcf = math.gcd(gcf, int(lst_creeper[i+1]))
    
print(gcf)
    