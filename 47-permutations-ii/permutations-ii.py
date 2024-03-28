class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        orderedperm = itertools.permutations(nums)
        ulofperm = []
        for perm in orderedperm:
            if perm not in ulofperm:
                ulofperm.append(perm)
        return ulofperm