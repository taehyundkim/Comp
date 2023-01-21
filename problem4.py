wall = list(map(int, input().split()))

inv = wall.copy()
inv.sort()
min = inv[0]

wall_size = len(wall)

wall_copy = [0]*wall_size
for i in range(wall_size):
    wall_copy[(i + min) % wall_size]= wall[i]
    
for i in range(len(wall_copy)):
    print(wall_copy[i], end=" ")