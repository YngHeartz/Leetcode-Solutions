# start from the end, if current char not a ' ' append to list until ' '.
# .strip() makes this "   fly me   to   the moon  " to this "fly me   to   the moon"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = []

        if len(s.strip()) == 1:
            return 1

        for char in s.strip() [::-1]:
                res.append(char)
                if char.isspace():
                    return len(res) -1
        
        if ' ' not in s.strip():
            return len(s.strip())
        print(res)
