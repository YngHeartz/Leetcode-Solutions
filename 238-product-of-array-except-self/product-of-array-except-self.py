class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        postfix = 1
        for num in range(len(nums)):
            res[num] = postfix
            postfix *= nums[num]
        
        prefix = 1
        for num in range(len(nums) -1, -1, -1,):
            res[num] *= prefix
            prefix *= nums[num]
        
        return res