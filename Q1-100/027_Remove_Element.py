"""
Notes:
    A simple application of two pointers, many way to realize that
    
Leetcode:
    None
"""
from typing import List


class Solution:
    """
    Two pointers:
        check every element, del the target

    Complexity:
        O(n)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        ls = len(nums)

        l = 0
        r = ls

        while l < r:
            if nums[l] == val:
                del nums[l]
                r -= 1
            else:
                l += 1

        return len(nums)


s = Solution()
print("Two pointers:")
print(s.removeElement([3, 2, 2, 3], 3))


##########################################################


class Solution:
    """
    Two pointers 2:
        check every element, remove the target

    Complexity:
        O(n)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)

        return len(nums)

s = Solution()
print("Two pointers 2:")
print(s.removeElement([3, 2, 2, 3], 3))