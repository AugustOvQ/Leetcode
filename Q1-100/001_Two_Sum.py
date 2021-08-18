"""
Notes:
    In real world application, we care about memory, not storage space
    Tey to use `dict`, `enumerate`, `zip` and `set`
    
Leetcode:
    https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
"""
from typing import List


class Solution:
    """
    Brute force:
        Nested loop traverse list twice

    Complexity:
        Time: n * (n-1) = O(n^2)
        Space: 1 = O(1)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


s = Solution()
print("Brute force:")
print(s.twoSum([3, 2, 4], 6))

##########################################################################


class Solution:
    """
    Hashmap:
        Go through 0 to n, and store the complement of each entry
        Go through 0 to n again, check if the entry is in the complement

    Complexity:
        Time: O(n)
        Space: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize hashmap as dictionary
        seen = {}

        for index, value in enumerate(nums):
            remaining = target - nums[index]

            if remaining in seen:
                return [seen[remaining], index]
            else:
                seen[value] = index


s = Solution()
print("Hashmap:")
print(s.twoSum([3, 2, 4], 6))

##########################################################################


class Solution:
    """
    A even faster solution

    Complexity:
        Time: O(n)
        Space: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_nums = dict()
        for index, value in enumerate(nums):
            reminder = target - value
            if reminder in dict_nums:
                return [dict_nums[reminder], index]
            dict_nums[value] = index


s = Solution()
print("Hashmap2:")
print(s.twoSum([3, 2, 4], 6))

##########################################################################


class Solution:
    """
    Sorted two pointers search:
        Two pointers start at `left` most and `right` most, get temp_sum
        if temp_sum==target, return
        if temp_sum>target, move the `right` pointer one step left
        if temp_sum<target, move the `left` pointer one step right   
        
    Complexity:
        O(n) 
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for left in range(len(numbers) - 1):
            right = len(numbers) - 1
            while left < right:
                temp_sum = numbers[left] + numbers[right]
                if temp_sum > target:
                    right -= 1
                elif temp_sum < target:
                    left += 1
                else:
                    return [left, right]


s = Solution()
print("Two pointers:")
print(s.twoSum([3, 2, 4], 6))
