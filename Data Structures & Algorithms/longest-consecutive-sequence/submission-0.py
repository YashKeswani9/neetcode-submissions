class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        for i in nums:
            streak = 0;
            current = i;
            while current in setNums:
                streak += 1
                current += 1
                res = max(res, streak)
        return res

        