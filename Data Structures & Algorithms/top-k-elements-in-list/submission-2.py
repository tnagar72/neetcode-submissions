import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # do some frequency counting
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        assert len(heap) == k

        result = [heapq.heappop(heap)[1] for idx in range(k)]
        return result

        
        