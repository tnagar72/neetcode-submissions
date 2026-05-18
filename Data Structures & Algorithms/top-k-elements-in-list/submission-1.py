from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for num in nums:
            dict[num] += 1
        
        sorted_keys = sorted(dict.items(), key= lambda x: x[1], reverse = True)

        return [sorted_keys[i][0] for i in range(k)]
