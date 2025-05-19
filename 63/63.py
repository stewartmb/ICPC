class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    elif i == 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    elif j == 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[n-1][m-1]
    
# Example usage:
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))  # Output: 2