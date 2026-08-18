class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')':'(', '}':'{', ']':'['}
        stack = []

        for p in s:
            if p in bracketMap.values():
                stack.append(p)
            else: 
                if len(stack) > 0:
                    current = stack.pop()
                    if current != bracketMap[p]:
                        return False
                else:
                    return False
        
        return len(stack) == 0 