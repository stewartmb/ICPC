class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        # Inicializar la matriz de DP n*n
        dp = [[0] * m for _ in range(n)]
        # Llenar la primera celda
        dp[0][0] = grid[0][0]
        # Llenar la primera fila
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        # Llenar la primera columna
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # Llenar el resto de la matriz
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[n-1][m-1]
# Test
grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
result = solution.minPathSum(grid)
print(result)  
        
