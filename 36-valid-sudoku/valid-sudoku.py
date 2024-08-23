class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num != '.':
                    row_key = f'{num} in row {row}'
                    col_key = f'{num} in col {col}'
                    subgrid_key = f'{num} in subgrid {row//3}{col//3}'

                    if row_key in seen or col_key in seen or subgrid_key in seen:
                        return False
                    
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(subgrid_key)
        
        return True