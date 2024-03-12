class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Check if the input value is less than or equal to zero; if so, return False
        if n <= 0:
            return False
        
        # Divide the input value by 3 until it's no longer divisible by 3.
        # If the result eventually becomes 1, the input number is a power of three, 
        # otherwise, it's not.
        while n % 3 == 0:
            n /= 3
        
        return n == 1