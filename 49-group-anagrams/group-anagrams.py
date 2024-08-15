# Create a defaultdict(list) to store the sorted key and the word as its values
# Create a loop that itterates over each item in the strs list
# Then we want to create a variable that stores the sorted word as a key if its not in the dict already
# We then append the word to the list
# Then return a list of sublists





class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())