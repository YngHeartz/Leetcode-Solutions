# height = [1, 6, 3, 7, 5, 4]
# calculate the amount of water that can be between two points, find the two points that can have the most water, update the max_water variable every time we move points, if value is greater than prev max_water,update max water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_water = max(max_water, width * min_height)

            # need to itterate over the height array left and right and not just left and right, instead of the position left and right. we need to check the values not just the position left and right
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water