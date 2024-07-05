from os import listdir, path
from sys import argv

def tree(file_path, states=[]):
    isdir = path.isdir(file_path)
    symbol = "+" if isdir else "-"
    for state in states:
        if   state == "mid":    print("| ", end="")
        elif state == "end":    print("  ", end="")
        elif state == "branch": print("|-", end="")
        elif state == "last":   print("'-", end="")
    print(symbol, file_path.split("/")[-1])
    if isdir:
        children = sorted(listdir(file_path))
        child_count = len(children)
        for index, child in enumerate(children):
            new_states = states.copy()
            if len(new_states):
                if   new_states[-1] == "branch": new_states[-1] = "mid"
                elif new_states[-1] == "last":   new_states[-1] = "end"
            if   index == child_count-1: new_states.append("last")
            elif index <  child_count-1: new_states.append("branch")
            tree(file_path+"/"+child, new_states)

def main():
    if len(argv) == 1:
        tree(".")
    elif len(argv) == 2:
        tree(argv[1])
    else:
        raise Exception("Invalid Usage: Use with one or two parameters")

if __name__ == "__main__":
    main()

