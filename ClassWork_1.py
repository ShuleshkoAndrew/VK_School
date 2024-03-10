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


# мы предполагаем, что arr1 - это изначально наибольший массив, расширенный до размера len(arr1) + len(arr2)
def economic_merge_sorted_arrays(arr1: list, arr2: list) -> list:
    pointer1 = len(arr1) - 1
    pointer2 = len(arr2) - 1
    pointer3 = len(arr1) - len(arr2) - 1

    while pointer2 >= 0:
        if pointer3 >= 0 and arr1[pointer3] > arr2[pointer2]:
            arr1[pointer1] = arr1[pointer3]
            pointer3 -= 1
        else:
            arr1[pointer1] = arr2[pointer2]
            pointer2 -= 1
        pointer1 -= 1

    return arr1


def even_first(arr: list) -> list:
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[even_index], arr[i] = arr[i], arr[even_index]
            even_index += 1

    return arr
