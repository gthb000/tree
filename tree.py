from os import listdir, path
from sys import argv

def tree(file_path, level=0):
    isdir = path.isdir(file_path)
    symbol = "+" if isdir else "-"
    print(level*"  ", symbol, " ", file_path.split("/")[-1], sep="")
    if isdir:
        for child in listdir(file_path):
            tree(file_path+"/"+child, level+1)

def main():
    if len(argv) == 1:
        tree(".")
    elif len(argv) == 2:
        tree(argv[1])
    else:
        raise Exception("Invalid Usage: Use with one or two parameters")

if __name__ == "__main__":
    main()

