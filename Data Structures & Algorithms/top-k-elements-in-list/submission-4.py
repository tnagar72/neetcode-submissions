from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # do some frequency counting
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        buckets = []
        for idx in range(len(nums) + 1):
            buckets.append([])

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        for idx in range(len(buckets) - 1, 0, -1):
            if len(buckets[idx]) != 0:
                result.extend(buckets[idx])

            if len(result) == k:
                return result

        
        