class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Create a set 'z' to store the unique elements of the input list 'nums'.
        z = set(nums)
        
        # Initialize an empty list 'x' to store the missing numbers.
        x = []
        
        # Iterate over numbers from 1 to the length of 'nums' (inclusive).
        for num in range(1, len(nums) + 1):
            # Check if the current number 'num' is not in the set 'z'.
            if num not in z:
                # If 'num' is missing, append it to the list 'x'.
                x.append(num)
        
        # Return the list of missing numbers.
        return x
