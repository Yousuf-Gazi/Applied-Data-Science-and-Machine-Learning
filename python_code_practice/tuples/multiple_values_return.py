# Example of returning multiple values using tuples
nums = (5, 10, 15, 20)


def min_max_sum(nums):
    return (
        min(nums),
        max(nums),
        sum(nums)
    )


if __name__ == '__main__':
    min, max, total = min_max_sum(nums)
    print(f"Min: {min}, Max: {max}, Sum: {total}")
