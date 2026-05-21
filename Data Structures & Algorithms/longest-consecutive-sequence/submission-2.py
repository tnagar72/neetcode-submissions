class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        max_length = 0

        for num in nums:
            hs.add(num)

        for idx, num in enumerate(nums):
            num_prev  = num - 1
            if (num - 1) in hs:
                continue
            
            flag = 1
            curr_length = 1
            curr_num = num
            while flag == 1:

                if (curr_num + 1) in hs:
                    curr_length += 1
                    curr_num += 1
                else:
                    flag = 0
            
            max_length = max(max_length, curr_length)


        return max_length

        