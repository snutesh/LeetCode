class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        first = 0
        last = rows*cols-1
        while first<=last:
            mid = int((first + last)/2)
            num = matrix[int(mid/cols)][mid % cols]
            if target == num:
                return True
            elif target < num:
                last = mid - 1
            else:
                first = mid + 1