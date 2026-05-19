class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # collect all the sizes together
        sizes  = ", ".join([str(len(s)) for s in strs])
        return sizes + "#" + ''.join(strs)



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        hash_index = s.index('#')

        sizes = s[:hash_index].split(", ")

        res = []

        i = hash_index + 1
        for size in sizes:
            j = i + int(size)
            res.append(s[i:j])
            i = j

        return res

