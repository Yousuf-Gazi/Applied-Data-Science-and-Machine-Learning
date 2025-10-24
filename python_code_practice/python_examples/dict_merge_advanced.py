# Merge dictionaries and sum numeric valuealues for duplicate keys
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}


def merge_sum(a, b):
    res = dict(a)
    for key, value in b.items():
        if key in res and isinstance(res[key], (int, float)) and isinstance(value, (int, float)):
            res[key] += value
        else:
            res[key] = value
    return res


if __name__ == '__main__':
    print("Merged:", merge_sum(a, b))
