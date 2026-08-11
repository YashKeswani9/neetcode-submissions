class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        smap = dict()
        print('hello')
        if n == m:
            for i in range(0, n, 1):
                count = smap.get(s[i], 0)
                count += 1
                smap[s[i]] = count

            print(smap)

            for j in range(0, m, 1):
                if t[j] not in smap:
                    return False
                
                count = smap.get(t[j])
                count -= 1
                smap[t[j]] = count

            print(smap)
            
            for i in smap.values():
                print(i)
                if i > 0:
                    return False
            
            return True
            
        return False

        