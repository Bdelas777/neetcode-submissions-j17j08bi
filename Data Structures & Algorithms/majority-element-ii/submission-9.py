from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        lista = []
        for key, val in freq.items():
            if val > len(nums) / 3:
                lista.append(key)
        return lista



