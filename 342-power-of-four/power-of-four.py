class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if the input value is less than or equal to zero; if so, return False
        if n <= 0:
            return False
        
        # Continuously divide the input value by 4 until it's no longer divisible by 4.
        # If the result eventually becomes 1, the input number is a power of four, 
        # otherwise, it's not.
        while n % 4 == 0:
            n /= 4
        
        return n == 1