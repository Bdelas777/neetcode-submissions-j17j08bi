class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc,tc = {},{}
        for index in range(len(s)):
            sc[s[index]] = 1 + sc.get(s[index],0)
            tc[t[index]] = 1 +tc.get(t[index],0)
        return tc == sc 

