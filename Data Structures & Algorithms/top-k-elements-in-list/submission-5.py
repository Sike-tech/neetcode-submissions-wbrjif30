class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            m[num] = m.get(num,0) + 1
        return sorted(m,key=lambda x : m[x], reverse= True)[:k]