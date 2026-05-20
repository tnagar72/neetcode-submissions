class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_list = [0] * 26
        freq_count = {}

        for s in strs:
            for char in s:
                freq_list[ord(char) - ord('a')] += 1
            freq_tuple = tuple(freq_list)

            if freq_tuple not in freq_count.keys():
                freq_count[freq_tuple] = list()
                freq_count[freq_tuple].append(s)
            else:
                freq_count[freq_tuple].append(s)
            freq_list = [0] * 26

        
        # recreate list

        
        return list(freq_count.values())
