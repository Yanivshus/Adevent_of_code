file = open("day1-input.txt", "r").readlines()
right = []
left = []
for line in file:
    line = line[0:len(line)-1]
    subline = line.split("   ")
    right.append(int(subline[1]))
    left.append(int(subline[0]))

right.sort()
left.sort()

total = 0

for i in range(0,len(right)):
    total += abs(right[i] - left[i])
print(total)

