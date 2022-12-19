inp = open("input.txt", "r")

rucksacks = []
for line in inp.readlines():
    rucksacks.append(line[:-1])

# Question 1

total = 0

for rucksack in rucksacks:
    compartment_1 = rucksack[:len(rucksack)//2]
    compartment_2 = rucksack[len(rucksack)//2:]

    common = list(set(compartment_1).intersection(set(compartment_2)))[0]

    if common in "qwertyuiopasdfghjklzxcvbnm":
        total += ord(common) - 96

    elif common in "QWERTYUIOPASDFGHJKLZXCVBNM":
        total += ord(common) - 38

print(total)

# Question 2

total = 0
groups = [rucksacks[x: x + 3] for x in range(0, len(rucksacks), 3)]

for group in groups:
    badge = list(set(group[0]).intersection(
        set(group[1])).intersection(set(group[2])))[0]

    if badge in "qwertyuiopasdfghjklzxcvbnm":
        total += ord(badge) - 96

    elif badge in "QWERTYUIOPASDFGHJKLZXCVBNM":
        total += ord(badge) - 38

print(total)
