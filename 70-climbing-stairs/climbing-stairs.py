class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2

        for _ in range(n - 1):
            temp = one
            one = two
            two = temp + two
        
        return one