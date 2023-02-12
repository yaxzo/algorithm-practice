"""
LINEAR SEARCH ALGORITHM
use if elem in array (list) < 100 (n < 100)
ARRAY MAY SORTED!!!
worst case O(n)
best case O(1)
avg case O(n / 2)
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_search(array: list, search_num: int):
    for i in range(len(array) - 1):
        if array[i] == search_num:
            return f"index {i}."
    return f"{search_num} not in list."


print(linear_search(arr, 8))
