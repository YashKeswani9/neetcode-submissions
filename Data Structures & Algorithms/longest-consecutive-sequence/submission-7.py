class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n-1) in numSet:
                continue
            start = 1
            while n+1 in numSet:
                n = n+1
                start += 1
            longest = max(longest, start)
        return longest 