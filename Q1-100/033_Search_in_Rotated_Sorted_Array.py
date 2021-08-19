"""
Notes:
    The first question about binary search, remember binary search
    is only applicable in sorted array, so make sure the part is 
    sorted (see if-else in solution)

Leetcode:
    https://www.geeksforgeeks.org/python-program-for-binary-search/
"""
from typing import List


class Solution:
    """
    Binary search:
        do binary search in the part the target should belong to
        
    Complexity:
        O(logn)
    """
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        n = len(nums)

        low, high = 0, n-1
        while low <= high:
            
            mid = (low + high)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1


s = Solution()
print("Binary search:")
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
