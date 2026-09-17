from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            group[key].append(strs[i])

        return list(group.values())
        
        