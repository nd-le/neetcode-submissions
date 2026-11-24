class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = {i:set() for i in range(len(board[0]))}
        col_sets = {i:set() for i in range(len(board[1]))}
        box_sets = {(i, j):set() for i in range(3) for j in range(3)}

        for row in range(len(board[0])):
            for col in range(len(board[1])):
                if board[row][col] == ".":
                    continue

                if (board[row][col] in row_sets[row] or
                    board[row][col] in col_sets[col] or
                    board[row][col] in box_sets[(row // 3, col // 3)]):
                    return False

                row_sets[row].add(board[row][col])
                col_sets[col].add(board[row][col])
                box_sets[(row // 3, col // 3)].add(board[row][col])

        return True