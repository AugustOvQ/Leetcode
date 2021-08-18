from typing import List


class Solution:
    """
    Simple two pointers:
        Left most and right most, choose the higher one as height,
        the difference of location as width
    Complexity:
        O(n)
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            result = max(min(height[left], height[right])
                         * (right - left), result)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result


s = Solution()
print("Simple greedy:")
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))

###########################################################


class Solution:
    def maxArea(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + \
                (height[l] == h), r - (height[r] == h)
        return res


s = Solution()
print("Simple greedy:")
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
print(s.maxArea([4, 3, 2, 1, 4]))
print(s.maxArea([1, 2, 1]))
