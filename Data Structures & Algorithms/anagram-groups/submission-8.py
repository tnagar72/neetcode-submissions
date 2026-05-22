class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for s in strs:
            freq_count = [0] * 26
            for char in s:
                freq_count[ord(char) - ord('a')] += 1

            mp[tuple(freq_count)].append(s)


        return (list(mp.values()))
        