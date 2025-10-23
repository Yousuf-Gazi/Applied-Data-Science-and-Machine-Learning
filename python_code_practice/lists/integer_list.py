# A simple list of integers and a small demo function.
integer_list = [1, 2, 3, 5, 8, 13, 21]


def sum_integers(integer_list):
    """Return the sum of integers in the list."""
    return sum(integer_list)


if __name__ == '__main__':
    print("Integer list:", integer_list)
    print("Sum:", sum_integers(integer_list))
