class Directory:
    def __init__(self, name):
        self.contents = []
        self.name = name

    def get_size(self):
        total = 0
        for object in self.contents:
            total += object.get_size()
        return total


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def get_size(self):
        return self.size


inp = open("day7/input.txt", "r")

root = Directory("/")
dir_stack = [root]
focused_dir = root

for line in inp.readlines():
    if line.startswith("dir "):
        focused_dir.contents.append(Directory(line[4:-1]))
    elif line == "$ cd /\n":
        focused_dir = dir_stack[0]
        dir_stack = []
    elif line.startswith("$ cd ") and line != "$ cd ..\n":
        for dir in focused_dir.contents:
            if dir.name == line[5: -1]:
                dir_stack.append(focused_dir)
                focused_dir = dir
    elif line == "$ cd ..\n":
        focused_dir = dir_stack.pop()
    elif line.split(" ")[0].isnumeric():
        focused_dir.contents.append(
            File(int(line.split(" ")[0]), line.split(" ")[1][:-1]))


# Question 1
small_dirs = []


def find_small_dirs(dir):
    if dir.get_size() <= 100000:
        small_dirs.append(dir)
    for obj in dir.contents:
        if type(obj) == Directory:
            find_small_dirs(obj)


find_small_dirs(root)
total = 0
for i in small_dirs:
    total += i.get_size()
print(total)

# Question 2
used_space = root.get_size()
total_size = 70000000
dirs = []
dirs_that_work = []


def find_all_dirs(dir):
    dirs.append(dir)
    for obj in dir.contents:
        if type(obj) == Directory:
            find_all_dirs(obj)


find_all_dirs(root)
smallest_gap = 9999999999999
best_dir = root
for i in dirs:
    if total_size - used_space + i.get_size() > 30000000:
        dirs_that_work.append(i)

best_dir = min(dirs_that_work, key=lambda i: i.get_size())
print(best_dir.get_size())
