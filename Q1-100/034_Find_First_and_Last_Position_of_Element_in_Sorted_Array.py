"""
Notes:
    Binary search, instaed of a number find the first and the last

Leetcode:
    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14714/16-line-Python-solution-symmetric-and-clean-binary-search-52ms
"""
from typing import List


class Solution:
    """
    Binary search:

    Complexity:
        O(logn)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLow(nums, target):
            low, high = 0, len(nums)-1
            res = -1
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    res = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return res

        def findHigh(nums, target):
            low, high = 0, len(nums)-1
            res = -1
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    res = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return res

        res_low = findLow(nums, target)

        if res_low == -1:
            return [-1, -1]

        res_high = findHigh(nums, target)

        return [res_low, res_high]


s = Solution()
print("Binary search:")
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
print(s.searchRange([1], 0))
