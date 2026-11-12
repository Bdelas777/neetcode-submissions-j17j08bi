class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapa = {}
        for i,n in enumerate(nums):
            busco = target - n
            if busco in mapa:
                return [mapa[busco],i]
            mapa[n] = i 