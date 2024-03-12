class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        i = 0
        for r in range(len(s) -1, -1 , -1):
            if s[i] == s[r]:
                i += 1
        
        if i == len(s):
            return s
        
        suffix = s[i:]
        prefix = suffix[::-1]
        return prefix + self.shortestPalindrome(s[:i]) + suffix