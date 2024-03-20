class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        left, right = 0, len(k) - 1

        while left <= right:
            if k[left] != k[right]:
                return False
            left += 1
            right -= 1
        return True