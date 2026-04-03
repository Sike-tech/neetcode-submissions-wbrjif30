class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            group[frozenset(Counter(word).items())].append(word) # group[key].append(word) (key -> same for anagrams since its a Counter of that word)
        return list(group.values())

        '''
        Counter(word).items does this
        {'e':1, 'a':1, 't':1} → [('e',1), ('a',1), ('t',1)] (makes the key-value pairs of Counter into tuples inside a list)
        and frozenset makes this immutable to allow it to be the key of a dictionary
        (keys have to be mutable)
        we only need to return a list of group anagrams so we only need values of our dictionary
        
        example input and output :-
        #input# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        #output# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        (each of these outputs was a value in the key-value pairs of the dictionary)
        (and keys for these values were their Counter() functions)
        Counter("eat") = {'e':1, 'a':1, 't':1}
        '''