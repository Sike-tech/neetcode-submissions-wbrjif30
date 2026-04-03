class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(Counter(nums),key=lambda x : Counter(nums)[x], reverse= True)[:k]