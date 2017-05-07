from tasks import sort
from random import randint


def main():
    print(sort.delay([randint(0, 20) for x in range(10)]))


if __name__ == "__main__":
    main()

