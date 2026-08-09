class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) == len (t)):
            dictionary = dict()
            for i in range(len(s)):
                if (s[i] in dictionary.keys()):
                    count = dictionary.get(s[i])
                    count += 1
                    dictionary.update({s[i] : count})
                else:
                    dictionary.update({s[i] : 1})
                
                if(t[i] in dictionary.keys()):
                    count = dictionary.get(t[i])
                    count -= 1
                    dictionary.update({t[i] : count})
                else:
                    dictionary.update({t[i] : - 1})
                print(dictionary)

            for key in dictionary.keys():
                print(dictionary)
                if(dictionary.get(key) != 0):
                    return False
            return True
        return False