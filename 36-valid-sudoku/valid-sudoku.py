class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create empty set we will add the keys to after each iteration
        seen = set()

        # checking every index in the 9 x 9 board
        for row in range(9):
            for col in range(9):
                # create a variable that will be holding the value at current index
                num = board[row][col]

                # if the value at the current index is not a "." meaning there is a number there we will add it to the seen set
                # if already in seen set we will return "False" because its an invalid sudoku.
                # if that condition is never met and all the values have been itterated over, we will return "True"
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