class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        newnums = []
        for num in range(1, len(nums) + 1):
            if num not in num_set:
                newnums.append(num)
        return newnums