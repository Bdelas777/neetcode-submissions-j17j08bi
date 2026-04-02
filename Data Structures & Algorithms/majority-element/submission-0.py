class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        sortedFreq = sorted(freq.items(), key=lambda item: item[1],reverse= True)
        return sortedFreq[0][0]