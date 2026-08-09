class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        colsize = len(matrix[0]) - 1 
        finalrow = -1 
        while top <= bottom:
            mid = (top + bottom)//2
            if target > matrix[mid][0]:
                if target > matrix[mid][colsize]:
                    top = mid + 1
                else:
                    finalrow = mid
                    break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif top == bottom:
                finalrow = top
                break
            elif matrix[mid][0] == target: 
                return True
        
        if finalrow != -1:
            l = 0;
            r = colsize;
            while l <= r:
                mid = (l + r)//2
                if target > matrix[finalrow][mid]:
                    l = mid + 1
                elif target < matrix[finalrow][mid]:
                    r = mid - 1
                elif target == matrix[finalrow][mid]:
                    return True
        return False
