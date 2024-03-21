class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use the find() method to search for the index of the needle in the haystack
        index = haystack.find(needle)
        
        # Return the index of the first occurrence of the needle in the haystack
        # If the needle is not found, find() returns -1, which will be returned as the result
        return index