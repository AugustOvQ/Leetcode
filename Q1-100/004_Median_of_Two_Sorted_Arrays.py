"""
Notes:
    written by my own, haven't check other solutions

Leetcode:

"""
from typing import Counter, List


class Solution:
    """
    Simple two pointers search:
        merge two arrays by pointers
        store the merged list only till the index of median
        get median


    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) >= len(nums2):
            left, right = nums1, nums2
        else:
            left, right = nums2, nums1

        m, n = len(left), len(right)
        single = True if (m+n) % 2 != 0 else False
        ls = (m+n)/2 if single else (m+n+1)/2

        l, r = 0, 0
        result = []
        while ls >= 0:
            if r == n:
                result.append(left[l])
                l += 1
            elif l == m:
                result.append(right[r])
                r += 1
            else:
                if left[l] <= right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1

            ls -= 1

        median = result[-1] if single else (result[-1] + result[-2])/2

        return median


s = Solution()
print("Pointers:")
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
print(s.findMedianSortedArrays([0, 0], [0]))
print(s.findMedianSortedArrays([], [1]))
print(s.findMedianSortedArrays([2], []))
