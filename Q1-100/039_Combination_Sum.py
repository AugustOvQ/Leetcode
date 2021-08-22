"""
Notes:
    First question on backtracking, but not the first in the list
    Go over other easier backtracking question first
    
Leetcode:
    https://leetcode.com/problems/combination-sum/discuss/429538/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
"""
from typing import List


class Solution:
    """
    Depth first decision tree:
        Two branches, each controls one frequency of an element

    Complexity:
        O(2^n)
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # continue
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # try other candidate
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res


s = Solution()
print("Backtracking:")
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum([1], 1))
print(s.combinationSum([1], 2))

############################################################


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i],
                     path + [candidates[i]], res)


s = Solution()
print("Backtracking 2:")
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2], 1))
print(s.combinationSum([1], 1))
print(s.combinationSum([1], 2))
