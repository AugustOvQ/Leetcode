import collections
from typing import Collection, List


class Solution:
    """
    Brute force
    
    Complexity:
        O(n^4)
    """

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ls = len(nums1)

        res = []
        for i in range(ls):
            for j in range(ls):
                for k in range(ls):
                    for l in range(ls):
                        sum_list = [nums1[i], nums2[j], nums3[k], nums4[l]]
                        s = sum(sum_list)

                        if s == 0:
                            res.append(sum_list)

        return len(res)


s = Solution()
print("Brute force:")
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))


###################################################################

class Solution:
    """
    Memory two+two sum:
    
    Complexity:
        O(n^2)
    """
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sums = collections.Counter(c+d for c in C for d in D)
        return sum(sums.get(-(a+b), 0) for a in A for b in B)
    
    
s = Solution()
print("Two linear:")
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))