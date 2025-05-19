class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_square = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        matrix[i][j] = 1
                        if max_square == 0:
                            max_square = 1
                    else:
                        matrix[i][j] = 0
                elif matrix[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    if matrix[i][j] > max_square:
                        max_square = matrix[i][j]
        return max_square * max_square
# Example usage:
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
solution = Solution()
print(solution.maximalSquare(matrix))  # Output: 4