from collections import defaultdict


def solution(board):
    columns = defaultdict(set)
    rows = defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] in rows[row] or board[col][row] in columns[col]:
                return False
            rows[row].add(board[row][col])
            columns[col].add(board[col][row])
    return True


if __name__ == '__main__':
    print(solution(board=[["1", "2", ".", ".", "3", ".", ".", ".", "."],
                          ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                          [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                          ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                          [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                          [".", ".", ".", ".", ".", ".", "2", ".", "."],
                          [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
