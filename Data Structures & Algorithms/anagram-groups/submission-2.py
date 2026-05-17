class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = dict()

        for element in strs:
            sorted_anagram = "".join(sorted(element))

            if sorted_anagram in anagram_dict.keys():
                anagram_dict[sorted_anagram].append(element)
            else:
                anagram_dict[sorted_anagram] = list()
                anagram_dict[sorted_anagram].append(element)

        
        return list(anagram_dict.values())


        