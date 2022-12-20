inp = open("input.txt", "r")

assignments = []

for line in inp.readlines():
    assignments.append(line[:-1])

# Question 1

total = 0

for assignment in assignments:
    elf1 = assignment.split(",")[0].split("-")
    elf2 = assignment.split(",")[1].split("-")

    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        total += 1

    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        total += 1

print(total)

# God I fucking love sets
# Question 2

total = 0

for assignment in assignments:
    elf1 = assignment.split(",")[0].split("-")
    elf2 = assignment.split(",")[1].split("-")

    range1 = set([i for i in range(int(elf1[0]), int(elf1[1]) + 1)])
    range2 = set([i for i in range(int(elf2[0]), int(elf2[1]) + 1)])

    if range1.intersection(range2) != set():
        total += 1

print(total)
