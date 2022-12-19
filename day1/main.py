inp = open("input.txt", "r")

elves = []
current_elf = 0

for line in inp.readlines():
    if line == "\n":
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)

elves.sort()

print(elves[-1])
print(elves[-1] + elves[-2] + elves[-3])
