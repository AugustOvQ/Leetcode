"""
Notes:
    Basically just sorted then apply a twosum algrorithm.
    Note to check duplicated list
    
Leetcode:
    https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).
"""
from typing import List


class Solution:
    """
    Hashmap:
        Sort
        Set first number as target, del it from list
        do twosum hashmap to the rest numbers
        avoid duplicated number signed to hashmap
        
    Complexity:
        Time: O(n^2)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_list = []
        target_set = set()
        while len(nums) >= 3:
            target = nums[0]
            del nums[0]
            if target in target_set:
                continue
            target_set.add(target)

            seen = {}
            remaining_set = set()
            for index, value in enumerate(nums):
                remaining = -target - value
                
                if remaining in seen and remaining not in remaining_set:
                    answer_list.append([target, remaining, value])
                    remaining_set.add(remaining)
                else:
                    seen[value] = index

        return answer_list


s = Solution()
print("Hashmap:")
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 0, 0, 0]))


############################################################

class Solution:
    """
    Sorted three pointers search:
        for each number, do twosum sorted pointers search
    
    Complexity:
        Time: O(n^2)
    
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_list = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    answer_list.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return answer_list
    
s = Solution()
print("Sorted pointer:")
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 0, 0, 0]))