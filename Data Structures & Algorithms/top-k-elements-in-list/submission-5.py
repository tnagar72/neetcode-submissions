class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_counter = {}

        for num in nums:
            freq_counter[num] = 1 + freq_counter.get(num, 0)
        

        freq_bucket = [list() for idx in range(len(nums) + 1)]

        for key, value in freq_counter.items():
            freq_bucket[value].append(key)

        res = []
        for idx in range(len(freq_bucket) - 1, -1, -1):
            res.extend(freq_bucket[idx])

            if len(res) == k:
                return res