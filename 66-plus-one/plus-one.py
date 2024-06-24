class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        
        # Add one to the integer
        number += 1
        
        # Convert the integer back to a list of digits and return
        return list(map(int, str(number)))