treasureMap = [int(element) for element in input().strip().split()]

# TODO
sum1 = 27492857294857394875289
ind1 = 0
smol1 = 0
sum2= 27492857294857394875289
ind2 = 0
smol2 = 0

for i in range(len(treasureMap) - 2):
    speed = treasureMap[i] + treasureMap[i+1] + treasureMap[i+2]
    smol = min(treasureMap[i], treasureMap[i+1], treasureMap[i+2])
    if speed < sum1:
        sum1 = speed
        ind1 = i
        smol1 = smol
    if speed == sum1 and i > ind1:
        sum2 = speed
        ind2 = i
        smol2 = smol

speed = treasureMap[-2] + treasureMap[-1] + treasureMap[0]
smol = min(treasureMap[-2] , treasureMap[-1] , treasureMap[0])
if speed < sum1:
    sum1 = speed
    ind1 = i
    smol1 = smol
if speed == sum1 and i > ind1:
    sum2 = speed
    ind2 = i
    smol2 = smol
    
speed = treasureMap[-1] + treasureMap[0] + treasureMap[1]
smol = min(treasureMap[1] , treasureMap[-1] , treasureMap[0])
if speed < sum1:
    sum1 = speed
    ind1 = i
    smol1 = smol
if speed == sum1 and i > ind1:
    sum2 = speed
    ind2 = i
    smol2 = smol
    
if sum1 < sum2:
    print(sum1, " ", ind1)
else:
    if smol1 < smol2:
        print(sum1, " ", ind1)
    elif smol2 > smol1: 
        print(sum2, " ", ind2)
    else:
        if ind1 < ind2:
            print(sum1, " ", ind1)
        else:
            print(sum2, " ", ind2)