from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        sub = defaultdict(set)
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    
                    if n in row[i] or n in col[j]:
                        print("row/col")
                        return False

                    row[i].add(n)
                    col[j].add(n)

                    sub_row = int(i / 3)
                    sub_col = int(j / 3)
                    if n in sub[(sub_row, sub_col)]:
                        print("sub")
                        return False
                    
                    sub[(sub_row, sub_col)].add(n)
        return True

                