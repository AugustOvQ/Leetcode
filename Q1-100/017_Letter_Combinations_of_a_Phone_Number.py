"""
Notes:
    Backtracking question
    
Leetcode:
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep
"""

from typing import List


class Solution:
    """
    Question:
        How to deal with the mapping num -> letters?
    Answer:
        Build a dictionary

    Backtracking:
        d

    Complexity:
        d
    """

    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping
        mapping = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        # Empty digits
        if len(digits) == 0:
            return []

        res = []
        self.dfs(digits, 0, mapping, '', res)

        return res

    def dfs(self, nums, index, mapping, path, res):
        if index >= len(nums):
            res.append(path)
            return
        
        letters = mapping[nums[index]]
        for i in letters:
            self.dfs(nums, index+1, mapping, path+i, res)


s = Solution()
print("Backtracking")
print(s.letterCombinations("23"))
