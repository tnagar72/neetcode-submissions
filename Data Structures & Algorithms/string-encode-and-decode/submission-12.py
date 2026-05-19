class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res



    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        length = 0
        idx = 0
        while idx < len(s):
            if s[idx] == '#':
                length = int(s[i: idx])

                string = s[idx + 1: idx + 1 + length]
                res.append(string)
                idx = i = idx + 1 + length
            idx += 1
        return res
            

