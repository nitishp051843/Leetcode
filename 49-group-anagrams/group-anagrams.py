class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagram = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            grouped_anagram[sorted_s] = grouped_anagram.get(sorted_s, []) + [s]
        return list(grouped_anagram.values())