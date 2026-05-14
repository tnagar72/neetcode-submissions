class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = dict()
        # Key would be the target number, value will be the number itself and the index of it

        for i in range(len(nums)):
            if nums[i] in targetDict:
                return [targetDict[nums[i]][1], i]
            else:
                targetDict[target - nums[i]] = (nums[i], i)
        
        return None