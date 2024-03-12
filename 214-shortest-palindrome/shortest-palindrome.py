class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Base case: If the input string is empty, return an empty string
        if not s:
            return ''
        
        # Initialize index `i` to track the length of the palindrome suffix
        i = 0
        
        # Iterate over the string `s` from the end towards the beginning
        for r in range(len(s) - 1, -1, -1):
            # Check if characters at index `i` and `r` are equal
            if s[i] == s[r]:
                i += 1
        
        # If `i` has traversed the entire string, it's already a palindrome
        if i == len(s):
            return s
        
        # Extract the non-palindromic suffix
        suffix = s[i:]
        # Reverse the suffix to get the prefix
        prefix = suffix[::-1]
        # Recursively construct the shortest palindrome by adding reversed prefix,
        # the shortest palindrome of the remaining prefix, and the original suffix
        return prefix + self.shortestPalindrome(s[:i]) + suffix