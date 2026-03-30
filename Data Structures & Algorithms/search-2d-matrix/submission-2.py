class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            m = (top+bottom) // 2
            if matrix[m][0] > target:
                bottom = m - 1
            elif matrix [m][-1] < target:
                top = m + 1
            elif matrix[m][0] <= target <= matrix[m][-1]:
                break
        
        l,r = 0, len(matrix[0])- 1
        
        while l <= r:
            n = (l+r)//2
            if matrix[m][n] < target:
                l = n + 1
            elif matrix[m][n] > target:
                r = n - 1
            elif matrix[m][n] == target:
                return True
        return False
        