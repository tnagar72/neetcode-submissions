class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count = 0
        left = 0
        right = len(nums) - 1

        while (left <= right):
            if left == right:
                if nums[right] == val:
                    count += 1
                break
            if nums[left] == val:
                if nums[right] == val:
                    count += 1
                    right -= 1
                    continue
                else:
                    # swap the values now
                    count += 1
                    nums[left] = nums[right]
                    nums[right] = val
                    left += 1
                    right -= 1
            else:
                left += 1

        if count == len(nums):
            del nums[:]
            return len(nums)
        if count != 0:
            del nums[-count:]
            return len(nums)
        return len(nums)

        

        