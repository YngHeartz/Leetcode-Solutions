class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        char_set = set()

        for char_s, char_t in zip(s, t):
            if char_s in char_dict:
                if char_dict[char_s] != char_t:
                    return False
            
            else:
                if char_t in char_set:
                    return False
                char_dict[char_s] = char_t
                char_set.add(char_t)
        
        return True