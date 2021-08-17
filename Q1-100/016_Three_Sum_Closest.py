"""
Notes: 
    Sorted pointers, check the closest sum
Leetcode:
    https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
"""
from typing import List


class Solution:
    """
    Sorted pointers + dict:
        Use sum as the index in the dict, the list as value
    Complexity:
        O(n^2)
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(ls-2):
            l, r = i+1, ls-1

            while l < r:
                temp = nums[i] + nums[l] + nums[r]

                if temp == target:
                    return target

                if abs(target - temp) < abs(target - res):
                    res = temp
                if temp < target:
                    l += 1
                else:
                    r -= 1

        return res


s = Solution()
print("Sorted pointer")
print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([0, 0, 0], 1))
