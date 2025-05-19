class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cod = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    cod[i] = max(cod[i], cod[j] + 1)
        return max(cod)
# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
solution = Solution()
result = solution.lengthOfLIS(nums)
print(result)  # Output: 4