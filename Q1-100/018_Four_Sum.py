"""
Notes:
    Similar to two sum and three sum, use four pointers 1+3 or 2+2?
    
Leetcode:

"""
from typing import List


class Solution:
    """
    Brute force:
        four nested loop, use sorted list to check duplicate

    Complexity:
        O(n^4), rejected by leetcode
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ls = len(nums)
        res = []

        for i in range(ls-3):
            for j in range(i+1, ls-2):
                for k in range(j+1, ls-1):
                    for l in range(k+1, ls):
                        s_list = [nums[i], nums[j], nums[k], nums[l]]
                        s = sum(s_list)

                        if s == target and s_list not in res:
                            res.append(s_list)

        return res


s = Solution()
print("Brute force:")
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))


##############################################################


class Solution:
    """
    Two pointers:
        nested loop of depth 2 + two pointers

    Complexty:
        O(n^3)
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ls = len(nums)
        res = []

        for i in range(ls - 3):
            for j in range(i+1, ls-2):
                l, r = j+1, ls-1

                while l < r:
                    sum_list = [nums[i], nums[j], nums[l], nums[r]]
                    s = sum(sum_list)

                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        if sum_list not in res:
                            res.append(sum_list)

                        l += 1

        return res


s = Solution()
print("Two pointers:")
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))


##############################################################


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.findNSum(nums, target, 4, [], res)
        return res

    def findNSum(self, nums, target, N, prefix, result):
        L = len(nums)
        if N == 2:
            l, r = 0, L-1
            while l < r:
                add = nums[l] + nums[r]
                if add == target:
                    result.append(prefix + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif add > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(L-N+1):
                if target < N*nums[i] or target > N*nums[-1]:  # key judgement
                    break
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    self.findNSum(nums[i+1:], target-nums[i],
                                  N-1, prefix+[nums[i]], result)
        return


s = Solution()
print("Two pointers 2:")
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))

##############################################################


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        ls = len(nums)
        res = []
        while i < ls-3:
            if target-nums[i] < 3*nums[i+1] or target-nums[i] > 3*nums[-1]:
                while i < ls-4 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
                continue
            j = i+1
            while j < ls-2:
                if target-nums[i]-nums[j] < 2*nums[j+1] or target-nums[i]-nums[j] > 2*nums[-1]:
                    while j < ls-3 and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                    continue
                left = j+1
                right = ls-1
                new_target = target-nums[i]-nums[j]
                while left < right:
                    if nums[left]+nums[right] > new_target:
                        right -= 1
                    elif nums[left]+nums[right] < new_target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        temp_left = nums[left]
                        temp_right = nums[right]
                        while(left < right and nums[left] == temp_left):
                            left += 1
                        while(left < right and nums[right] == temp_right):
                            right -= 1
                while j < ls-3 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i < ls-4 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


s = Solution()
print("Two pointers 3:")
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([2, 2, 2, 2, 2], 8))
