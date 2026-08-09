class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        i , j = 0 , length - 1
        while i < j:
            if (numbers[i] + numbers[j] == target):
                return [i+1, j+1]
            while (numbers[i] + numbers[j] > target):
                j -= 1
            while (numbers[i] + numbers[j] < target):
                i += 1