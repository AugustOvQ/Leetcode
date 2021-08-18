"""
Notes:
    Start from brute force, noticing that the hight is min(x, y)
    and the width is diff(x, y). So start from left most and right most
    greedily.
    
Leetcode:
    https://www.youtube.com/watch?v=UuiTKBwPgAo
"""
from typing import List


class Solution:
    """
    Brute force:
        Check every combination, loop of depth 2

    Complexity:
        O(n^2), rejected by leetcode
    """

    def maxArea(self, height: List[int]) -> int:
        res = 0

        ls = len(height)
        for l in range(ls):
            for r in range(l+1, ls):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res


s = Solution()
print("Brute force:")
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))

###########################################################


class Solution:
    """
    Simple two pointers:
        Start from left most and right most, shift the pointer leave the
        pointer with lower height

    Complexity:
        O(n)
    """

    def maxArea(self, height: List[int]) -> int:
        res = 0
        ls = len(height)
        l, r = 0, ls-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


s = Solution()
print("Simple greedy:")
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))
