import numpy as np


def binary_search(sorted_list, item):
    min = 0
    pos = 0
    max = len(sorted_list) - 1
    center = int((max - min) / 2)

    i = 0
    while min != max:
        i += 1

        if item < sorted_list[center]:
            max = center
            center = int((max - min) / 2) + pos

        else:
            min = center + 1
            pos = min
            center = int((max - min) / 2) + pos

        if sorted_list[center] == item:
            return center, i

    return center, i


def binary_search1(sorted_list, item):
    min = 0
    max = len(sorted_list) - 1

    i = 0
    while min <= max:
        i += 1

        # I dont need to keep pos

        mid = int((min + max) / 2)
        guess = sorted_list[mid]

        if guess == item:
            return mid, i

        if guess > item:
            max = mid - 1
        else:
            min = mid + 1

    return -1, i


def main():
    sorted_list = list(range(0, 12))

    time = []

    for item in range(0, 12):
        pos, iteration = binary_search(sorted_list, item)
        time.append(iteration)

        print("Position of %d is :%d (%d)" % (item, pos, iteration))

    print(np.max(time))
    print(np.sum(time))

    time = []

    for item in range(0, 12):
        pos, iteration = binary_search1(sorted_list, item)
        time.append(iteration)

        print("Position of %d is :%d (%d)" % (item, pos, iteration))

    print(np.max(time))
    print(np.sum(time))


if __name__ == "__main__":
    main()
