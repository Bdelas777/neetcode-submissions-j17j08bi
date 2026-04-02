class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        
        # Empty string is always segmentable
        dp[0] = True
        
        # Iterate through all possible substring lengths
        for i in range(1, n + 1):
            # Check all possible splits of the substring
            for j in range(i):
                # If previous substring is segmentable and current substring is in dictionary
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        # Return whether entire string can be segmented
        return dp[n]

                