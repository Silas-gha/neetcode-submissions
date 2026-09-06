class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return(False)
        S_Count={}
        for i in s:
            if i in S_Count:
                S_Count[i] += 1
            else:
                S_Count[i]=1
        for j in t:
            if j in S_Count:
                if S_Count[j] > 0:
                    S_Count[j] -=1
                else:
                    return(False)
            else:
                return(False)

        return(True)
                