class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1

        # print(left, right)

        while left <= right:
            # if left == right:
            #     if nums[right] == val:
            #         count += 1
            #     break
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

        print(count, nums, right)
        del nums[len(nums) - count:]
        return len(nums)

        

        