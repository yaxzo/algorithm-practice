"""
BINARY SEARCH ALGORITHM
if elem in array (list) exm. 100.000 - need 17 comparison

worst case O(log n) 
best case O(1)
avg case O(log n)
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(array: list, search_num: int):
    left, right = 0, (len(array) - 1)

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == search_num:
            return f"index {mid}."
        else:
            if array[mid] < search_num:
                left = mid + 1
            else:
                right = mid + 1
    else:
        return f"{search_num} not in list."


print(binary_search(arr, 8))
