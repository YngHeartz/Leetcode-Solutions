class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == ' ':
            return True
        s = ''.join(letter for letter in s if letter.isalnum())
        s = s.lower()
        print(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True