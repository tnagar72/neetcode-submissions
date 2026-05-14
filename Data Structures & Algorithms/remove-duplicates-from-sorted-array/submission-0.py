class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx1 = 0
        idx2 = 0

        while idx2 < len(nums) - 1:
            current = nums[idx1]
            if nums[idx1 + 1] == current:
                idx2 = idx1 + 1
            else:
                idx1 += 1
                idx2 = idx1
                continue

            while nums[idx2] == nums[idx1]:
                nums.pop(idx2)
                if not(idx2 < len(nums)):
                    break
            idx1 = idx2
        
        return len(nums)

        