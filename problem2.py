fish_input = input().split(" ")

fish_input.sort()
a = []

tally = 1
for i in range(0, len(fish_input) - 1):
    if fish_input[i+1] == fish_input[i] + 1:
        tally+=1
    else
        a.append(tally)
        tally = 1

a.sort()

print(a[-1])
