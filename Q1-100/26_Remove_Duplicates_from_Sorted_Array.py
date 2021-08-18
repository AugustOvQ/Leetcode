"""
Notes:
    When first see "duplicates" in list we should always think about
    turn list into set
    
Leetcode
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/507271/Simple-Python-beats-100
"""
from typing import List


class Solution:
    """
    Brute force:
       Remove duplicates directly by .remove()

    Complexity:
        O(n)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        ls = len(nums)

        for i in range(ls-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.remove(nums[i])

        return len(nums)


s = Solution()
print("Brute force:")
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


#############################################################

class Solution:
    """
    List to set:
        Use the non-duplicatable property of set

    Complexity:
        O(n)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))

        return len(nums)


s = Solution()
print("List to set:")
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
