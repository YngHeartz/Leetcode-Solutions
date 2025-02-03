class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create array, initiazlized to the length of nums. filled with 1's
        res = [1] * len(nums)

        # create a postfix that will then be used to take numbers from nums 
        # multiply the postfix by the num in nums and then replace the res num with the new postfix
        postfix = 1
        for num in range(len(nums)):
            res[num] = postfix
            postfix *= nums[num]
        
        # do the same thing as the postfix but do it to the numbers before current index
        
        prefix = 1
        for num in range(len(nums) -1, -1, -1):
            res[num] *= prefix
            prefix *= nums[num]
        
        return res