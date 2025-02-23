def search_2d_matrix(matrix, target):
    l, r = 0, len(matrix) - 1

    while l <= r:
        mid = (l + r) // 2

        first_value = matrix[mid][0]
        last_value = matrix[mid][-1]

        if target < first_value:
            r = mid - 1
        elif target > last_value:
            l = mid + 1
        else:
            if target in matrix[mid]:
                return True
            else:
                return False
    return False


print(search_2d_matrix(
    matrix=[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40], [41, 42, 45, 50], [50, 51, 52, 53], [54, 55, 56, 57]],
    target=50))
