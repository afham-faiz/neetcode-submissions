class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        T = []
        S = []
        for j in t:
            T.append(j)
        for k in s:
            S.append(k)

        for i in s:
            if i in T:
                T.remove(i)
                S.remove(i)
        
        if T == [] and S == []:
            return True
        else:
            return False