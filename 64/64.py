
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        # Inicializar la matriz de DP n*n
        dp = [[0] * n for _ in range(n)]
        # Llenar la primera fila y columna
        for i in range(n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # Completar M
        for i in range(1, n):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # Resultado
        return dp[n-1][n-1]
    
# Test
grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
result = solution.minPathSum(grid)
print(result)  
        
