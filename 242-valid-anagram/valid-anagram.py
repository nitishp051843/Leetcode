class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for i in s:
            countS[i] = countS.get(i, 0) + 1
        for i in t:
            countT[i] = countT.get(i, 0) + 1
        for i in countS:
            if i not in countT:
                return False
            if countS[i] != countT[i]:
                return False

        return True
        