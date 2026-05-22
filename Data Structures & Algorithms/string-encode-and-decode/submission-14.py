class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:

        i = 0
        j = 0
        res = []
        length_string = 0

        while j < len(s):
            if s[j] != '#':
                j += 1
                continue
            else:
                length_string = int(s[i:j])
                each_string = s[j+1:j+1+length_string]
                res.append(each_string)
                i = j + 1 + length_string
                j = i

        return res
