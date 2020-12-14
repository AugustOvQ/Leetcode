from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize hashmap
        compliments = {}
        # Initialize result
        result = []

        for index, num in enumerate(nums):
            if compliments.get(num) is None:  # Hashmap not have the number
                compliments[target - num] = index
            else:
                result = [compliments[num], index]
        return result


s = Solution()
print(s.twoSum([2, 7, 11, 15], 26))

# {24:0, 19: 1, 15: 2}
# we have 15
# return
