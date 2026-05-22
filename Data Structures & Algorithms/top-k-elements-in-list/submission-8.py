class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)

        for num in nums:
            map[num] += 1

        freq_count = [list() for idx in range(len(nums)+1)]

        for key, value in map.items():
            freq_count[value].append(key)

        res = []
        for idx in range(len(freq_count) - 1, -1, -1):
            res.extend(freq_count[idx])

            if len(res) == k:
                return res

