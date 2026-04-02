class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupli = []
        for i in nums:
            if i in dupli:
                return True
            dupli.append(i)
        return False