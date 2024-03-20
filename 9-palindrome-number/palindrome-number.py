class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Initialize a variable 'k' which holds the string version of integer 'x'.
        k = str(x)
        
        # Initialize two variables 'left' and 'right' to traverse through the string.
        # 'left' starts at the first position of the string and 'right' starts at the end of the string.
        left, right = 0, len(k) - 1
        
        # Create a while loop that continues as long as 'left' is less than or equal to 'right'.
        while left <= right:
            # Check if the character at 'left' is not equal to the character at 'right'.
            # If they are not equal, return False as it is not a palindrome.
            if k[left] != k[right]:
                return False
            
            # Move 'left' pointer one step to the right and 'right' pointer one step to the left.
            left += 1
            right -= 1
        
        # If the loop completes without finding any unequal characters, return True as it is a palindrome.
        return True
