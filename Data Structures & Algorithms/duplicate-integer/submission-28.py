class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lista = set()
        for n in nums:
            if n in lista:
                return True 
            lista.add(n)
        return False
        