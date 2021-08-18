"""
Notes:
    Similar to two sum and three sum, use four pointers 1+3 or 2+2?
    
Leetcode:

"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer_list = []
        nums.sort()
        for i in range(len(nums)-3):
            for j in (i+1, len(nums)-3):
                l, r = j+1, len(nums)-1
                
                while l < r:
                    s = nums[i] + nums[j] + nums[r] + nums[r]
                    
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        answer_list.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1
                        
        return answer_list
    
s = Solution()
print("Four pointers:")
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 0))
    