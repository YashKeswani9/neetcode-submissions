class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        listOperators = ['+', '-', '*', '/']
        stack = []
        res = 0
        for c in tokens:
            if c not in listOperators:
                stack.append(c)
            else:
                operandTwo = stack.pop();
                operandOne = stack.pop();
                if c == '+':
                    res = int(operandOne) + int(operandTwo)
                elif c == '-':
                    res = int(operandOne) - int(operandTwo)
                elif c == '*':
                    res = int(operandOne) * int(operandTwo)
                elif c == '/':
                    res = int(operandOne) / int(operandTwo)
                stack.append(res)
        return int(stack[-1])