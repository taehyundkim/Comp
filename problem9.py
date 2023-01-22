n = int(input())
sticks = [int(element) for element in input().strip().split()]

# TODO
sticks.sort()

print(max(sticks[0] + sticks[-1], sticks[n//2] + sticks[n//2 + 1]))