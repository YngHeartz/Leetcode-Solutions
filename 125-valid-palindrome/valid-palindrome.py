class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Check if the input string is empty or contains only whitespace, if so, it's considered a palindrome
        if s == ' ':
            return True
        
        # Remove non-alphanumeric characters from the string and convert it to lowercase
        s = ''.join(letter for letter in s if letter.isalnum())
        s = s.lower()
        
        # Initialize two pointers, one pointing to the start of the string and the other to the end
        left, right = 0, len(s) - 1
        
        # Iterate through the string from both ends towards the middle
        while left < right:
            # If characters at current positions don't match, the string is not a palindrome
            if s[left] != s[right]:
                return False
            # Move the pointers towards the middle
            left += 1
            right -= 1
        
        # If the loop completes without finding any mismatch, the string is a palindrome
        return True