"""
Notes:
    First sorting problem, can use normal sorting algorithms or pointers
    
Leetcode:
    https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Bubble sorting:
            In-place bubble sort

        Complexity:
            O(nlog(n))
        """
        ls = len(nums)

        for i in range(ls):
            already_sorted = True

            for j in range(ls-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

                    already_sorted = False

            if already_sorted:
                break

        return nums


s = Solution()
print("Bubble sort:")
print(s.sortColors([2, 0, 2, 1, 1, 0]))
print(s.sortColors([1, 0, 1]))


##########################################################

class Solution:
    """
    Two pointers:
        Only 1, 2, 3 in nums, so when we see 0 we move it left most
        when we see 2 move it right most, when left = right = 1 we search for a non-1 value

    Complexity:
        O(n)
    """

    def sortColors(self, nums: List[int]) -> None:
        ls = len(nums)

        l, r = 0, ls-1

        while l < r:
            # Check left = 0 or right = 2
            if nums[l] == 0:
                l += 1
            elif nums[r] == 2:
                r -= 1
            # Check left = 2 or right = 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            elif nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            # Check if left = right = 1, search for a non 1 value
            else:
                n = r-1
                while l < n:
                    if nums[n] != 1:
                        nums[r], nums[n] = nums[n], nums[r]
                        break
                    n -= 1

                if n == l:
                    break

        return nums


s = Solution()
print("Two pointers:")
print(s.sortColors([2, 0, 2, 1, 1, 0]))
print(s.sortColors([1, 0, 1]))


##########################################################

class Solution:
    """
    Three pointers:
        Sign three pointers, terminate when two pointers collide

    Complexity:
        O(n)
    """

    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        return nums


s = Solution()
print("Three pointers:")
print(s.sortColors([2, 0, 2, 1, 1, 0]))
print(s.sortColors([1, 0, 1]))
