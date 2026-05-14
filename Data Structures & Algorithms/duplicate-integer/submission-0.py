class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsDict = dict()

        for i in nums:
            if i in numsDict:
                return True
            else:
                numsDict[i] = i
        
        return False