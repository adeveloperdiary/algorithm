"""
Running Time: O(nlogn)

Design:
1. Sorting the array in descending order will help to construct the required numbers.
2. Used merge sort,which has running time to O(nlogn)
3. Finally there is one loop to go through the sorted list and create the two numbers
4. Total Running Time:
    = O(nlogn+n)
    = O(n[logn+1])
    = O(nlogn)
"""


def merge(left, right):
    i = 0
    j = 0

    out = []

    for _ in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] >= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1

    out += right[j:]
    out += left[i:]

    return out


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if input_list == []:
        return -1, -1

    sorted_arr = merge_sort(input_list)

    num1 = []
    num2 = []

    for i in range(0, len(sorted_arr), 2):
        num1.append(str(sorted_arr[i]))
        if i < len(sorted_arr) - 1:
            num2.append(str(sorted_arr[i + 1]))

    return int("".join(num1)), int("".join(num2))


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[0, 0, 0, 0, 0], [0, 0]])
test_function([[], [-1, -1]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
