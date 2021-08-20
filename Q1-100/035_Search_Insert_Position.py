"""
Notes:
    Simple binary search

Leetcode:
    None, written by my self
"""
from typing import List


class Solution:
    """
    Binary search:
        return mid, if not found, return low or high

    Complexity:
        O(logn)
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low


s = Solution()
print("Binary search")
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
print(s.searchInsert([1], 0))
