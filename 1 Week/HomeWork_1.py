def push_zeros(marks: list) -> list:
    zero_index = len(marks) - 1
    for i in range(len(marks) - 1, -1, -1):
        if marks[i] == 0:
            marks[i], marks[zero_index] = marks[zero_index], marks[i]
            zero_index -= 1
    return marks


print(push_zeros([5, 3, 2, 1, 0, 0, 5, 0, 0, 5, 5, 4, 4, 0, 0, 0]))
