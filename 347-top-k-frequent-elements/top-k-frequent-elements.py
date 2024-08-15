# Create a defaultdict(int) to store the count of each number
# Use a for loop to itterate over each number in nums and update the count to each number
# Create a variable to store the result in that will be a heap and get all the key values and sort them based on the largest count and then return the k amount of values




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        result = heapq.nlargest(k, count.keys(), key=count.get) [:k]
        
        return result