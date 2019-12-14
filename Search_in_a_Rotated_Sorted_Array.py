"""
Running Time :
    1. O(nlogn)

Design:
1. This is similar to Binary Search, where we find the target value based on the mid point
2. The only difference is, we have additional logic while trying to decide which side ( left, right ) to use for recursion.
3. Hence the running time is same as

"""


def search(input_list, number, start, end):
    # Base Conditions - Start

    if start > end:
        return -1

    if start == end and input_list[0] == number:
        return start

    if end - start == 1:
        if input_list[start] == number:
            return start
        elif input_list[end] == number:
            return end
        else:
            return -1

    # Base Conditions - End

    mid = (start + end) // 2

    if input_list[mid] == number:
        return mid
    else:
        if input_list[mid - 1] < input_list[start]:
            # left has the rotated pivot
            if number <= input_list[mid - 1] or number >= input_list[mid - 1]:
                # Still search in left
                return search(input_list, number, start, mid - 1)
            else:
                # Search in right
                return search(input_list, number, mid + 1, end)
        elif input_list[start] <= number <= input_list[mid - 1]:
            # default binary search condition ( left )
            return search(input_list, number, start, mid - 1)

        if input_list[mid + 1] > input_list[end]:
            # right has the rotated pivot
            if number >= input_list[mid + 1] or number <= input_list[end]:
                # Still search in right
                return search(input_list, number, mid + 1, end)
            else:
                # Search in left
                return search(input_list, number, start, mid - 1)

        elif input_list[mid + 1] <= number <= input_list[end]:
            # default binary search condition ( right )
            return search(input_list, number, mid + 1, end)

        return -1


def rotated_array_search(input_list, number):
    return search(input_list, number, 0, len(input_list) - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[], 1])  # New Test Case
test_function([[3, 4, 6, 7, 8, 9, 10, 1, 2], 1])  # New Test Case
test_function([[9, 10, 1, 2, 3, 4, 6, 7, 8], 10])  # New Test Case
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
