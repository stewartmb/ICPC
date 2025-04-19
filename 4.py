class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = len1 + len2
        mitad = n // 2
        left, right = 0, len1 - 1
        
        while True:
            mid1 = (left + right) // 2
            mid2 = mitad - mid1 - 2
            
            n1L = nums1[mid1] if mid1 >= 0 else float("-inf")
            n1R = nums1[mid1 + 1] if (mid1 + 1) < len1 else float("inf")
            n2L = nums2[mid2] if mid2 >= 0 else float("-inf")
            n2R = nums2[mid2 + 1] if (mid2 + 1) < len2 else float("inf")
            
            if n1L <= n2R and n2L <= n1R:
                if n % 2 == 1:
                    return min(n1R, n2R)
                return (max(n1L, n2L) + min(n1R, n2R)) / 2
            elif n1L > n2R:
                right = mid1 - 1
            else:
                left = mid1 + 1
