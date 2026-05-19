class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        suffix_product = []
        prod = 1
        #calculating prefix product
        for num in nums:
            prod *= num
            prefix_product.append(prod)
        
        prod = 1
        for idx in range(len(nums) - 1, -1, -1):
            prod *= nums[idx]
            suffix_product.append(prod)

        assert(len(suffix_product) == len(nums)) 
        res = []
        prod = 1
        for idx in range(len(nums)):
            if idx == 0:
                prod = suffix_product[len(nums) - 2 - idx]
            elif idx == (len(nums) - 1):
                prod = prefix_product[idx - 1]
            else:
                prod = prefix_product[idx - 1] * suffix_product[len(nums) - 2 - idx]
            res.append(prod)

        return res