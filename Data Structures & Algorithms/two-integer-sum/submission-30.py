class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            busco = target - n
            if busco in prevMap:
                return [prevMap[busco],i]
            prevMap[n] = i         






       