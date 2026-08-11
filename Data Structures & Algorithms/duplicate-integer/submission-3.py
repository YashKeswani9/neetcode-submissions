class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nmap = set()

        for n in nums:
            if n in nmap:
                return True
            
            nmap.add(n)
        return False