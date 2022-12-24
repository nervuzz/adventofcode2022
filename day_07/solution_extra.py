"""
--- Day 7: No Space Left On Device ---
--- Part Two ---
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


disk_space_avail = 70000000
min_unused = 30000000

free_space = disk_space_avail - root.size
to_free_up = min_unused - free_space
match_size = [d.size for d in root.all_dirs if d.size > to_free_up]

print(f"Options: {match_size}")
print(f"The smallest fit is: {min(match_size)}")

# Output:
# Options: [8021608, 8465165, 26391313, 4964676, 14470980, 11212301, 4825246, 9067124, 4419451, 7330912, 4370655]
# The smallest fit is: 4370655
