class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        ans = []
        for i,n in enumerate(nums):
            find = target - n
            if find in prevMap.keys():
                ans.append(prevMap[find])
                ans.append(i)
                return ans
            
            prevMap[n] = i
        