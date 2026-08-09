class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = float('inf')
        while l <= r:
            print(l)
            m = (l + r)//2
            minimum = min(nums[m], minimum)
            print(minimum)
            if (nums[m] >= nums[l] and nums[m] > nums[r]):
                l = m + 1
            else:
                r = m - 1
        return minimum