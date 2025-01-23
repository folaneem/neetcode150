from collections import defaultdict


def solution(board):
    columns = defaultdict(set)
    rows = defaultdict(set)
    square = defaultdict(set)

    for row in range(9):
        for col in range(9):
            cell = board[row][col]
            if cell == '.':
                continue
            if cell in columns[col] or cell in rows[row] or cell in square[(row // 3, col // 3)]:
                return False
            columns[col].add(cell)
            rows[row].add(cell)
            square[(row // 3, col // 3)].add(cell)
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
