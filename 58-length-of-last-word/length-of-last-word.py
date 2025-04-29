class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = []

        for char in s.strip() [::-1]:
            res.append(char)

            if char.isspace():
                return len(res) - 1
        
        if ' ' not in s.strip():
            return len(res)