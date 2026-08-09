class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIndex = 0
        n = len(s)

        isPal = [[False] * n for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                print(i, j)
                if (s[i] == s[j] and ((j - i) <=2 or isPal[i+1][j-1])):
                    isPal[i][j] = True
                    if resLen < j - i + 1: 
                        resIndex = i
                        resLen = j - i + 1
        
        return s[resIndex: resIndex + resLen]