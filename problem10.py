info = [int(element) for element in input().strip().split()]
foodchain = [[int(element) for element in input().strip().split()] for _ in range(info[1])]

# TODO
f = 0
a = []
b = []
c = []

for i in foodchain:
    if i[1] > info[0] or i[2] > info[0]:
        f += 1
        #print(f)
    elif i[1] == i[2] and i[0] == 2:
        f += 1
        #print(f)
    else:
        if i[0] == 1:
            if i[1] == i[2]:
                if (i[1] not in a) and (i[1] not in b) and (i[1] not in c):
                    a.append(i[1])
            else:
                if (i[1] in a) and (i[2] in b or i[2] in c):
                    f += 1
                elif (i[1] in b) and (i[2] in a or i[2] in c):
                    f += 1
                elif (i[1] in c) and (i[2] in a or i[2] in b):
                    f+= 1
                else:
                    if(i[1] in a):
                        a.append(i[2])
                    elif(i[1] in b):
                        b.append(i[2])
                    elif(i[1] in c):
                        c.append(i[2])
                    elif (i[2] in a):
                        a.append(i[1])
                    elif (i[2] in b):
                        b.append(i[1])
                    elif (i[2] in c):
                        c.append(i[1])
                    else:
                        a.append(i[1])
                        a.append(i[2])
        else:
            if (i[1] in b and i[2] in a) or (i[1] in c and i[2] in b) or (i[1] in a and i[2]  in c):
                f += 1
                #print(f)
            else:
                if (i[1] in a):
                    b.append(i[2])
                elif (i[1] in b):
                    c.append(i[2])
                elif (i[1] in c):
                    a.append(i[2])
                elif (i[2] in a):
                    c.append(i[1])
                elif (i[2] in b):
                    a.append(i[1])
                elif (i[2] in c):
                    b.append(i[1])
                    
print(f)
