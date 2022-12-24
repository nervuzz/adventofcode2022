"""
--- Day 7: No Space Left On Device ---
https://adventofcode.com/2022/day/7
"""
from dataclasses import dataclass, field


def read_dataset() -> list:
    with open("dataset", "r") as fp:
        yield from [line.strip() for line in fp.read().splitlines()]


@dataclass
class SysObj:
    """Base sys object"""
    name: str
    abs_path: str = ""
    size: int = 0
    all_dirs: list = field(default_factory=list)
    parent: object = None
    is_dir: bool = field(default=False)


@dataclass
class Dir(SysObj):
    """A directory"""
    is_dir: bool = True
    items: list[SysObj] = field(default_factory=list)

    def add_item(self, obj: SysObj):
        obj.parent = self
        obj.abs_path = self.abs_path + "/" + obj.name
        self.items.append(obj)
        self.update_size_tree(self, obj.size)
        if obj.is_dir:
            root.all_dirs.append(obj)

    @staticmethod
    def update_size_tree(obj, item_size):
        obj.size += item_size
        if obj.parent:
            obj.update_size_tree(obj.parent, item_size)


@dataclass
class File(SysObj):
    """A file"""
    extension: str = field(default="")


root = Dir("/", "/")
cd = root

for cmd in read_dataset():
    if cmd.startswith("$ cd"):
        dirname = cmd.removeprefix("$ cd ")
        if dirname == "..":
            cd = cd.parent
        else:
            for i in cd.items:
                if i.name == dirname:
                    cd = i
                    break
    elif cmd.startswith("$ ls"):
        ...
    elif cmd.startswith("dir"):
        dirname = cmd.removeprefix("dir ")
        cd.add_item(Dir(dirname))
    else:
        size, name = cmd.split()
        name, _, ext = name.partition(".")
        cd.add_item(File(name, cd.abs_path+"/"+name, int(size), extension=ext))

dirs_at_most_100000 = [d.size for d in root.all_dirs if d.size <= 100000]

print(dirs_at_most_100000)
print(f"The sum of their total sizes is {sum(dirs_at_most_100000)}")

# Output:
# [69927, 21479, 17334, 90468, 90468, 2835, 81548, 2835, 31414, 31414, 58850, 98354, 29399, 45275, 81528,
# 81528, 81528, 20745, 50029, 74948, 52503, 95245, 93199, 69766, 81815, 10557, 33980, 57545, 72379, 19204,
# 10968, 87468, 10297, 26778]
# The sum of their total sizes is 1783610
