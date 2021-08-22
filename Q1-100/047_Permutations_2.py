"""
Notes:
    Use i>0 and nums[i] == nums[i-1] to avoid duplicates
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        
        return res
    
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            res.append(path)
            
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
            
s = Solution()
print("Backtracking:")
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))