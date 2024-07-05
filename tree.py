from os import listdir, path
from sys import argv

class State:
    MID    = 0
    END    = 1
    BRANCH = 2
    LAST   = 3

def tree(file_path, states=[]):
    isdir = path.isdir(file_path)
    symbol = "+" if isdir else "-"
    for state in states:
        if   state == State.MID:    print("| ", end="")
        elif state == State.END:    print("  ", end="")
        elif state == State.BRANCH: print("|-", end="")
        elif state == State.LAST:   print("'-", end="")
    print(symbol, file_path.split("/")[-1])
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
            tree(file_path+"/"+child, new_states)

def main():
    if len(argv) == 1:
        tree(".")
    elif len(argv) == 2:
        tree(argv[1].rstrip("/"))
    else:
        raise Exception("Invalid Usage: Use with one or two parameters")

if __name__ == "__main__":
    main()

