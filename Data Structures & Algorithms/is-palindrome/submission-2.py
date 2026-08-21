class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and self.isAlphaNum(s[i]) != True:
                i += 1
            
            while i < j and self.isAlphaNum(s[j]) != True:
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1 
            j-=1
        return True
        
    def isAlphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9') or
            ord('a') <= ord(c) <= ord('z')):
            return True