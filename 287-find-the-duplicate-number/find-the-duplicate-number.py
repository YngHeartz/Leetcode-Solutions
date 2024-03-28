class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for num in range(1, len(nums)):
            if nums[num] == nums[num - 1]:
                return nums[num]