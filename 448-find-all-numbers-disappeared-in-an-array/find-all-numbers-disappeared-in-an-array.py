class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        z = set(nums)
        x = []
        for num in range(1, len(nums) + 1):
            if num not in z:
                x.append(num)
        return x