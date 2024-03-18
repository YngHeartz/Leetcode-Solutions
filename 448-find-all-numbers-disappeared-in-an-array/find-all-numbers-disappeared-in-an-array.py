class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # We remove duplicates by converting the nums list into a set.
        num_set = set(nums)
        
        # We initialize an empty list to store missing numbers.
        missing_nums = []
        
        # We iterate over each number from 1 to the length of nums.
        for num in range(1, len(nums) + 1):
            # If the current number is not in the num_set, it's missing, so we add it to the missing_nums list.
            if num not in num_set:
                missing_nums.append(num)
        
        return missing_nums
