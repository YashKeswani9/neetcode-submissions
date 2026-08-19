class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        listOperators = ['+', '-', '*', '/']
        stack = []

        for t in tokens:
            if t not in listOperators:
                stack.append(t)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                if t == '+':
                    res = operand1 + operand2
                elif t == '*':
                    res = operand1 * operand2
                elif t == '/':
                    res = operand1 / operand2
                elif t == '-':
                    res = operand1 - operand2
                
                stack.append(res)
        
        return int(stack.pop())
