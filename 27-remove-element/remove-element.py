# remove val from the list
# count the remaining length of list after removed
# return length and the new array

# problem is when we delete a item from the list, we skip a value from the itteration

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums:
            while val in nums:
                nums.remove(val) 
        return len(nums)