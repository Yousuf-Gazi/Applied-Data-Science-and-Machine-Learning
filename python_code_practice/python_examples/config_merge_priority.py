# Merge configuration dicts with priority: higher overrides lower
def merge_configs(*configs):
    result = {}
    for config in configs:
        result.update(config)
    return result


if __name__ == '__main__':
    print(merge_configs({'a': 1, 'b': 2}, {'b': 3}, {'c': 4}))
