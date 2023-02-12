"""
BUBBLE SORT ALGORITHM
use if elem in array (list) < 100 (n < 100)

avg case O(n * n)
"""

arr = [1, 5, 3, 2, 6, 7, 8, 10, 9, 4]


def bubble_sort(array: list) -> list:
    arr_len = len(array)

    for i in range(arr_len - 1):
        for j in range(arr_len - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


print(bubble_sort(arr))
