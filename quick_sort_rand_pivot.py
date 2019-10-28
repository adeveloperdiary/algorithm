import random

i = 0


def quick_sort(array):
    global i
    i += 1

    length = len(array)

    if length < 2:
        return array
    else:

        ptr = random.randint(0, length - 1)

        pivot = array[ptr]

        del array[ptr]

        left = [i for i in array if i <= pivot]
        right = [i for i in array if i > pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    array = list(range(900, 0, -1))

    '''
    array = []
    length = 12

    for i in range(0, length):
        array.append(random.randint(0, length - 1))
    '''

    print(array)
    sorted_array = quick_sort(array)

    print(sorted_array)
    print("Steps Taken %d" % i)


if __name__ == "__main__":
    main()
