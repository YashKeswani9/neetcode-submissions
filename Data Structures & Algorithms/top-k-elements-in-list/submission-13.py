class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n,0) + 1
        
        for n in countMap.keys():
            index = countMap[n]
            count[index].append(n)
        
        res = []
        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

