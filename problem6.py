info = [int(element) for element in input().strip().split()]
dest = info[0]
n = info[1]
routes = [[int(element) for element in input().strip().split()] for _ in range(n)]

# TODO
num_stops = -1
inter = []
for lst in routes:
    if inter == []:
        if lst[0] == 1:
            if lst[1] == dest:
                num_stops = 0
                break
            else:
                inter.append(lst[1])
                num_stops += 2
    elif len(inter) == 1: 
        if lst[0] == inter[0]:
            if lst[1] == dest:
                break
            else:
                inter.append(lst[1])
                num_stops += 1
    elif len(inter) == 2:
        if lst[0] == inter[1]:
            if lst[1] == dest:
                break
            else:
                inter.append(lst[1])
                num_stops += 1
    elif len(inter) == 3:
        if lst[0] == inter[2]:
            if lst[1] == dest:
                break
            else:
                inter.append(lst[1])
                num_stops += 1
    
print(num_stops)