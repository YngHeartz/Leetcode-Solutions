class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num != '.':
                    rk = f'{num} in row {row}'
                    ck = f'{num} in col {col}'
                    sg = f'{num} in subgrid {row//3}{col//3}'

                    if rk in seen or ck in seen or sg in seen:
                        return False
                    
                    seen.add(rk)
                    seen.add(ck)
                    seen.add(sg)
        
        return True