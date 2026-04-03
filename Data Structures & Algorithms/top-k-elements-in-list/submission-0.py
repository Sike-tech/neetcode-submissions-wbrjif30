class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        large = sorted(freq.keys(), key=lambda x: freq[x], reverse = True)
        output=[]
        for i in range(k):
            output.append(large[i])
        return output
