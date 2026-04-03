class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word)) # "eat", "tea", "ate" all → ('a','e','t')
            anagrams[key].append(word) # at the key = ('a','e','t') the words that match that key are added one by one ("eat","tea","ate")

        return list(anagrams.values())
