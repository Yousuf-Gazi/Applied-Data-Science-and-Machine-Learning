# Split a list into chunks of size n
def chunks(random_list, n):
    for i in range(0, len(random_list), n):
        yield random_list[i:i + n]


if __name__ == '__main__':
    print(list(chunks(list(range(10)), 3)))
