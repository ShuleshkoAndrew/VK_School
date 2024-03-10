def reverse_array(arr: list, left_pointer: int, right_pointer: int):
    # left_pointer = 0
    # right_pointer = len(arr) - 1
    while left_pointer < right_pointer:
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
        right_pointer -= 1
    # return arr


def cycle_reverse_array(arr: list, k: int) -> list:
    n = len(arr)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k % n - 1)
    reverse_array(arr, k % n, n - 1)

    return arr


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    merged_arrays = []
    i_1, i_2 = 0, 0

    while i_1 < len(arr1) and i_2 < len(arr2):
        if arr1[i_1] < arr2[i_2]:
            merged_arrays.append(arr1[i_1])
            i_1 += 1
        else:
            merged_arrays.append(arr2[i_2])
            i_2 += 1

    merged_arrays += arr1[i_1:]
    merged_arrays += arr2[i_2:]

    return merged_arrays


def


print(merge_sorted_arrays([3, 8, 10, 11], [1, 7, 9]))
