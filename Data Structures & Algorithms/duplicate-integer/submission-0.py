class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        example = []
        for i in nums:
            if i in example:
                return True
            example.append(i)
        return False