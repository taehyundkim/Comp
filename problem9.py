n = int(input())
sticks = [int(element) for element in input().strip().split()]

# TODO
sticks.sort()

if n % 2 == 0:
    print(max((sticks[0] + sticks[-1]), (sticks[n//2] + sticks[n//2 - 1])))
else:
    print(max((sticks[0] + sticks[-1]), (sticks[n//2] + sticks[n//2 + 1])))