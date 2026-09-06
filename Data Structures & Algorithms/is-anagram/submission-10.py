class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        SortedS=sorted(s)
        SortedT=sorted(t)

        if len(s) != len(t):
            return(False)

        for i, Val_i in enumerate(SortedS):
            if Val_i!=SortedT[i]:
                return(False)
        
        return(True)
    