class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = {}
        max_length = 0
        length = 0
        for num in nums:
            if num not in hs:
                if (num + 1) not in hs and (num - 1) not in hs:
                    hs[num] = 1
                if (num + 1) in hs and (num - 1) not in hs:
                    hs[num] = hs[num + 1] + 1
                    hs[num + hs[num + 1]] = hs[num]
                if (num - 1) in hs and (num + 1) not in hs:
                    hs[num] = hs[num - 1] + 1
                    hs[num - hs[num - 1]] = hs[num]
                if (num - 1) in hs and (num +1) in hs:
                    hs[num] = 1 + hs[num - 1] + hs[num + 1]
                    hs[num + hs[num + 1]] = hs[num]
                    hs[num - hs[num - 1]] = hs[num]

                max_length = max(hs[num], max_length)


        return max_length

        