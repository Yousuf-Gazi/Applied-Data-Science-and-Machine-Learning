# Use dict values as sets to collect unique items per key
data = [("a", 1), ("b", 2), ("a", 2), ("b", 3)]
d = {}
for key, value in data:
    d.setdefault(key, set()).add(value)


if __name__ == '__main__':
    print(d)
