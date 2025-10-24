# Use collections.defaultdict to group items.
from collections import defaultdict


pairs = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
grouped = defaultdict(list)
for key, value in pairs:
    grouped[key].append(value)


if __name__ == '__main__':
    print("Grouped:", dict(grouped))
