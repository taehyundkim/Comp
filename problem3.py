line1 = input().split(" ")
h = int(line1[0])
w = int(line1[1])
lines = []

for i in range(h):
    lines.append(input())
    
# TODO
'''
oxxox
xoxxx
oxxxx
xxxxo
'''
if (h < 4 or w < 5):
    print("-1 -1")
else:
    ans_x = -1
    ans_y = -1
    
'''
    for x in range(h):
        for y in range(w):
            if lines[x][y] == "o" and h-x >= 4 and w-y >= 5:
                ans_x = x 
                ans_y = y
'''