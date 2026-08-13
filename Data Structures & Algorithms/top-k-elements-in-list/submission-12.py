class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        countMap = {}
        ans = []

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)
        

        for num, count in countMap.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
