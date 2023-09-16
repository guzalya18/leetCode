class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sw = ''.join(sorted(i))
            res[sw].append(i)
        return list(res.values())
