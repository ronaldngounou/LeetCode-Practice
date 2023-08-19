class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n = len(mat)
        sum = 0
        for i in range(n):
            sum += mat[i][i]
            sum += mat[i][n-i-1]
        
        if n%2 == 1:
            sum -= mat[n//2][n//2]
        
        return sum
