"""
Notes:
    Structured solution

Leetcode:
    https://redquark.org/leetcode/0031-next-permutation/
"""
from typing import List, Literal


class Solution:
    """
    Structured solution

    Complexity:
        O(n)
    """

    def nextPermutation(self, nums):
        ls = len(nums)

        # First element that is smaller than its right
        index = ls-1
        while index > 0 and nums[index-1] >= nums[index]:
            index -= 1

        # Check if ascending
        if index == 0:
            nums.reverse()
            return nums

        # First element that is larger than nums[index]
        key = ls-1
        while nums[key] <= nums[index-1]:
            key -= 1

        # Reverse index-1 and key
        nums[index-1], nums[key] = nums[key], nums[index-1]

        # Reverse from index till the end
        l, r = index, ls-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums


s = Solution()
print("Brute force:")
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([3, 2, 1]))
print(s.nextPermutation([1, 1, 5]))
print(s.nextPermutation([1, 3, 2]))
print(s.nextPermutation([1, 1]))
print(s.nextPermutation([1]))
