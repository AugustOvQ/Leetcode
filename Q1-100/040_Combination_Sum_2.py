"""
Notes:
    Backtracking + avoid duplication
    
Leetcode:
    https://leetcode.com/problems/combination-sum-ii/discuss/17020/Python-easy-to-understand-backtracking-solution
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] > target:
                break

            self.dfs(nums[i+1:], target-nums[i], path + [nums[i]], res)


s = Solution()
print("Backtracking:")
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
