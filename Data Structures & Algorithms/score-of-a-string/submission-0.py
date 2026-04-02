class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for x in range(len(s) - 1):
            score += abs(ord(s[x + 1]) - ord(s[x]))
        return score
