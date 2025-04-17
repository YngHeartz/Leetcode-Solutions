class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check if s and t are same length
        if len(s) != len(t):
            return False

        # char dict and char set
        char_map = {}
        chared_set = set()


        # create zip of the s and t values.
        # if char s in char map check if the s value is not equal to the associated value to its key
        # if its not return False
        for char_s, char_t in zip(s, t):
            if char_s in char_map:
                if char_map[char_s] != char_t:
                    return False
            # if char s not in char_map
            # check if char t is in the char set
            # if char t in char set return False
            # update the char dict and char set
            else:
                if char_t in chared_set:
                    return False
                char_map[char_s] = char_t
                chared_set.add(char_t)
        
        return True