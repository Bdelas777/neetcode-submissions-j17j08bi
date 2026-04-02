class Solution:
    def reverse(self, x: int) -> int:
        reverse = str(abs(x))[::-1]
        reverInt = int(reverse)
        if  x < 0:
            reverInt = -reverInt
        if reverInt < -2**31 or reverInt > 2**31 -1:
            return 0
        return reverInt