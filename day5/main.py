inp = open("input.txt", "r")

# Question 1
# Parse input into 9 lists
rows = []
stacks = []
for i in range(9):
    rows.append(list(inp.readline())[:-1])

for col in range(len(rows[0])):
    potential_stack = ""
    for row in rows:
        potential_stack += row[col]
    if potential_stack[-1].isnumeric():
        stacks.append(list(reversed(list(potential_stack.strip()[:-1]))))

inp.readline()  # Remove blank line in input

# The actual logic

line = inp.readline()
while line != "":
    line = line[:-1]
    numbers = [int(i) for i in line.split(" ") if i.isnumeric()]
    temp_stack = []
    for i in range(numbers[0]):
        temp_stack.append(stacks[numbers[1] - 1].pop())
    temp_stack.reverse()
    stacks[numbers[2] - 1] += temp_stack
    line = inp.readline()

for i in stacks:
    print(i[-1], end="")
