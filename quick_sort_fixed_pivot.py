i = 0


def quick_sort(array):
    global i
    i += 1

    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    array = list(range(1000, 0, -1))

    sorted_array = quick_sort(array)

    print(sorted_array)
    print("Steps Taken %d" % i)


if __name__ == "__main__":
    main()
