class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i,num in enumerate(strs):
            key = ''.join(sorted(num))
            if key not in d:
                d[key] = []
            d[key].append(num)
        return list(d.values())