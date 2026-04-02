class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        sortedFreq = sorted(freq.items(), key=lambda item: item[1],reverse= True)
        stack = []
        for j in range(k):
            stack.append(sortedFreq [j][0])
        return stack

        
        
       