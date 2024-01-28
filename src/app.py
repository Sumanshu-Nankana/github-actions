import sys


def addition(*args):
    return sum(args)


if __name__ == "__main__":
    args = sys.argv[1:]
    numbers = list(map(int, args))
    result = addition(*numbers)
    print(f"The addition of {list(numbers)} are {result}")
