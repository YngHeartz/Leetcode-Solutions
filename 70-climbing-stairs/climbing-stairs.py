class Solution:
    def climbStairs(self, n: int) -> int:
        #  two variables that will be set to one
        # for each number in range of n - 1
        # create a variable that will store the last number we were on so that when we shift the 
        # b variable it will be equal to the last number and we will then add the numbers together and store that into the temp variable until we reach the last value in range of n and then return a since it will the the number of combinations it takes to reach n
        
        a, b = 1, 1

        for _ in range(n - 1):
            temp = a
            a = a + b
            b = temp
        
        return a