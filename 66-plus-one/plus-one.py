class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []

        for num in digits:
            res.append(str(num))
        
        comb = ''.join(res)

        comb = int(comb) + 1

        final = list(map(int, str(comb)))

        return final