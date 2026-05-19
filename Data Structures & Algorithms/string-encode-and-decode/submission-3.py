class Solution:

    def encode(self, strs: List[str]) -> str:
        non_ascii = "$#"
        if not strs:
            return "empty"
        return non_ascii.join(strs)

    def decode(self, s: str) -> List[str]:
        if "empty" == s:
            return []
        non_ascii = "$#"
        return s.split(non_ascii)
