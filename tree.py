from os import listdir, path
from sys import argv

class State:
    MID    = 0
    END    = 1
    BRANCH = 2
    LAST   = 3

class Color:
    DEFAULT = "\033[0m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[94m"
    @classmethod
    def by_id(cls, _id):
        return [
            cls.DEFAULT,
            cls.RED,
            cls.GREEN,
            cls.YELLOW,
            cls.BLUE,
        ][_id]
    @classmethod
    def paint(cls, color, text):
        return color+text+cls.DEFAULT

def tree(file_path, states=[], max_depth=0):
    isdir = path.isdir(file_path)
    symbol = "+" if isdir else "-"
    for level, state in enumerate(states):
        indent = "  "
        if   state == State.MID:    indent = "| "
        elif state == State.END:    indent = "  "
        elif state == State.BRANCH: indent = "|-"
        elif state == State.LAST:   indent = "'-"
        print(Color.paint(Color.by_id(level%4+1), indent), end="")
    print(symbol, file_path.split("/")[-1])
    if max_depth != 0 and len(states) >= max_depth: return
    if isdir:
        children = sorted(listdir(file_path))
        child_count = len(children)
        for index, child in enumerate(children):
            new_states = states.copy()
            if len(new_states):
                if   new_states[-1] == State.BRANCH: new_states[-1] = State.MID
                elif new_states[-1] == State.LAST:   new_states[-1] = State.END
            if   index == child_count-1: new_states.append(State.LAST)
            elif index <  child_count-1: new_states.append(State.BRANCH)
            tree(file_path+"/"+child, new_states, max_depth)

def help():
    print("""
Usage:
    
    python3 tree.py
    python3 tree.py <file>
    python3 tree.py <file> <max_depth>
""")

def main():
    if len(argv) == 1:
        tree(".")
    elif len(argv) == 2:
        if argv[1] == "/":
            tree("/")
        else:
            tree(argv[1].rstrip("/"))
    elif len(argv) == 3:
        if argv[2].isdigit():
            max_depth = int(argv[2])
        else:
            help()
        if argv[1] == "/":
            tree("/", max_depth=max_depth)
        else:
            tree(argv[1].rstrip("/"), max_depth=max_depth)
    else:
        help()

if __name__ == "__main__":
    main()

