class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountDict = {}
        numList = []
        for n in nums:
            if(n in numCountDict):
                count = numCountDict.get(n) 
                count += 1
                numCountDict[n] = count
            else:
                numCountDict[n] = 1
        
        print(numCountDict)
        numCountDictReverse = defaultdict(list)

        for key, value in numCountDict.items():
            numCountDictReverse[value].append(key)
        print(numCountDictReverse)
        
        counts = list(numCountDictReverse.keys())
        print(counts)
        counts.sort(reverse=True)
        print(counts)
        for n in counts:
            numList.extend(numCountDictReverse[n])
            if(len(numList) == k):
                break
        print(numList)
        return numList
        