class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return(False)
        S_Count={}
        T_Count={}
        for i in s:
            if i in S_Count:
                S_Count[i] += 1
            else:
                S_Count[i]=1
                
        for j in t:
            if j in T_Count:
                T_Count[j] += 1
            else:
                T_Count[j]=1
        print(S_Count)
        print(T_Count)
        if S_Count==T_Count:
            return(True)
        else:
            return(False)

                