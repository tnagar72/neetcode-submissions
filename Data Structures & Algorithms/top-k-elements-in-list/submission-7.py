import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_counter = {}

        for num in nums:
            freq_counter[num] = 1 + freq_counter.get(num, 0)
        
        heap = []

        for key, val in freq_counter.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [el[1] for el in heap]