class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        flag1 = 0
        flag2 = 0

        for num in nums:
            if num == 0:
                if flag1 == 0:
                    flag1 = 1
                    continue
                elif flag1 == 1:
                    flag2 = 1
                    break

            prod *= num

        res = []

        for num in nums:
            if flag1 == 1:
                if num == 0:
                    if flag2 == 1:
                        return [0] * len(nums)
                    elif flag2 == 0:
                        res.append(prod)
                else:
                    res.append(0)
            
            else:
                res.append(int(prod/num))
        return res   