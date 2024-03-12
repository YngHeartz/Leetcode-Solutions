class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if the input value is less than or equal to zero; if so, return False
        if n <= 0:
            return False
        
        # Continuously divide the input value by 2 until it's no longer divisible by 2.
        # If the result eventually becomes 1, the input number is a power of two, 
        # otherwise, it's not.
        while n % 2 == 0:
            n /= 2
        
        return n == 1