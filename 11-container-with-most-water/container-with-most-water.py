class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Initialize left and right pointers and a variable to store the maximum water
        left, right = 0, len(height) - 1
        max_water = 0

        
        
        # Iterate while left pointer is less than right pointer
        # Calculate the width as the distance between left and right
        # Determine the height by taking the smaller value between height[left] and heigh[right]
        # Update max_water with the larger of the current max_water or the area calculated

        while left < right:
            width = right - left
            heights = min(height[left], height[right])
            max_water = max(max_water, width * heights)

            # Move the left pointer if height[left] is smaller, otherwise move the right pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water