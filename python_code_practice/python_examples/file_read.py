# Simulate reading lines from a file using a list.
lines = ["first line\n", "second line\n", "third line\n"]

if __name__ == '__main__':
    for index, line in enumerate(lines, 1):
        print(index, line.strip())
