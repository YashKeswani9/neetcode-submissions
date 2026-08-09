class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']': '['}

        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif (stack[-1] == closeToOpen[c]):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False