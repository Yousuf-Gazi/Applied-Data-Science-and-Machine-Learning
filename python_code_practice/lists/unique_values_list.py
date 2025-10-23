# Create a list with duplicates and show how to get unique values preserving order
dup_list = [3, 1, 4, 1, 5, 9, 3, 5]


def unique_preserve_order(dup_list):
    seen = set()
    out = []
    for item in dup_list:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


if __name__ == '__main__':
    print("Original:", dup_list)
    print("Unique (order preserved):", unique_preserve_order(dup_list))
