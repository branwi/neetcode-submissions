class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        target = "W" if color == "B" else "B"
        rows = len(board)
        cols = len(board[0])
        directions = [
            (0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1, 1), (-1,-1)
            ]
        stack = deque([])
        for i in range(8):
            stack.append((rMove, cMove, i, 1))

        while stack:
            curr_r, curr_c, d, l = stack.popleft()
            cr, cc = directions[d]
            new_r, new_c = curr_r + cr, curr_c + cc

            if 0 <= new_r < len(board) and 0 <= new_c < len(board):
                if board[new_r][new_c] == target:
                    stack.append((new_r, new_c, d, l + 1))
                elif board[new_r][new_c] == ".":
                    continue
                elif board[new_r][new_c] == color:
                    if l >= 2:
                        return True
                    continue
        return False
