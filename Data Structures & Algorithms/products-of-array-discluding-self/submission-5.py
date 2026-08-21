class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        res = [1] * len(nums)

        for i in range(1, len(nums)): 
            prefix *= nums[i-1]
            res[i] = prefix
        
        for i in range((len(nums) - 2), -1, -1):
            postfix *= nums[i+1]
            res[i] *= postfix
        
        return res