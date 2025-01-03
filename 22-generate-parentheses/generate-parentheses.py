class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # create res list, add the valid pairs to this list
        res = []

        # backtrack function that will add the values to res if the len of string matches the len of n * 2 (all pairs have been matched and is proper length)
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                res.append(current)
                return
            
            # if the open bracket count is less than n we will add an open bracket until the count is == to n
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            # if the close count is less than the open count(not a valid pair) we will add the corresponding closing bracket to current(string we are working on)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return res