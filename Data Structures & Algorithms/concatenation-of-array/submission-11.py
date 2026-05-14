class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # we loop through the nums array twice

        array = [0] * 2*len(nums)
    
        for i, el in enumerate(nums):
            array[i] = array[i + len(nums)] = el

        return array