class Solution:
    def isValid(self, s: str) -> bool:
        
        while any(bracket_pair in s for bracket_pair in ['()', '{}', '[]']):
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
            
        
        if len(s) == 0:
            return True
        else:
            return False