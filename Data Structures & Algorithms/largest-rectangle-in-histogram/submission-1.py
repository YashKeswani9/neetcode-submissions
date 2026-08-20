class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                index, h = stack.pop()
                maxArea = max(maxArea, h*(i - index))
                start = index
            stack.append((start, n))
        
        for (i, h) in stack:
            maxArea = max(maxArea, h*(len(heights)- i))
        
        return maxArea