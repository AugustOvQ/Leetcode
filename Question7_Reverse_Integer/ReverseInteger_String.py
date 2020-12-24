class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        else:
            if x < 0:
                negative = True
                x *= -1
            x_rev = int(str(x)[::-1])
            if negative:
                x_rev *= -1
            if x_rev >= 2 ** 31 - 1 or x_rev <= -2 ** 31:
                return 0
            return x_rev


s = Solution()
print(s.reverse(1534236469))
