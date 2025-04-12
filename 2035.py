from itertools import combinations
import bisect

class Solution(object):
    def minimumDifference(self, nums):

        n = len(nums)
        k = n // 2
        total = sum(nums)
        left = nums[:k]
        right = nums[k:]
        
        left_sums = {i: [] for i in range(len(left) + 1)}
        right_sums = {i: [] for i in range(len(right) + 1)}
        
        for i in range(0, len(left) + 1):
            for comb in combinations(left, i):
                left_sums[i].append(sum(comb))
        
        for i in range(0, len(right) + 1):
            for comb in combinations(right, i):
                right_sums[i].append(sum(comb))
                
        for i in range(len(right) + 1):
            right_sums[i].sort()
        
        best = float("inf")
        
        for i in range(0, k + 1):
            left_list = left_sums[i]
            right_list = right_sums[k - i]
            for s in left_list:
                target_right = (total // 2) - s
                idx = bisect.bisect_left(right_list, target_right)
                if idx < len(right_list):
                    curr = s + right_list[idx]
                    diff = abs(total - 2 * curr)
                    if diff < best:
                        best = diff
                        if best == 0:
                            return 0
        return best
