class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        
        for element in nums:
            if element != val:
                tmp.append(element)
        
        nums[:len(tmp)] = tmp
        return len(tmp)
        