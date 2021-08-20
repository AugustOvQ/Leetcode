"""
Notes:
    Hash-map or sliding window
    
Leetcode:
    https://www.geeksforgeeks.org/window-sliding-technique/
"""
from typing import NoReturn


class Solution:
    """
    Hash-table:

    Complexity:
        O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        seen = {}

        left, right = 0, 0
        while right < n:
            # if unique
            if s[right] not in seen or left > seen[s[right]]:
                res = max(res, right-left+1)
                seen[s[right]] = right
                right += 1
            else:
                left = seen[s[right]]+1
                res = max(res, right-left+1)

        return res


s = Solution()
print("Hash-table:")
print(s.lengthOfLongestSubstring("abcabcbb"))


###########################################################


class Solution:
    """
    Hash-table 2:

    Complexity:
        O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length


s = Solution()
print("Hash-table 2:")
print(s.lengthOfLongestSubstring("abcabcbb"))


class Solution:
    """
    Sliding window:

    Complexity:
        O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        k = 1
        index = 0
        while index+k < n:
            if len(set(s[index:index+k+1])) == len(s[index:index+k+1]):
                k += 1
            else:
                index += 1
        return k


s = Solution()
print("Sliding window:")
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbb"))
