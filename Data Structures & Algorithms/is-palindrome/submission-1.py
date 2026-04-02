class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in s:
            if i.isdigit() or i.isalpha():
                new += i.lower()
        return (new == new[::-1])
        