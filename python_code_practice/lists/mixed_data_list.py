# A list that contains mixed data types
mixed_list = [42, "hello", 3.14, True, None]


def describe_list(mixed_list):
    return [(type(x).__name__, x) for x in mixed_list]


if __name__ == '__main__':
    print("Mixed list description:", describe_list(mixed_list))
