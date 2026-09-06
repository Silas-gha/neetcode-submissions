class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return(False)
        Array=[0]*26
        for i in s:
            index=ord(i)-ord("a")
            Array[index] += 1
        for i in t:
            index=ord(i)-ord("a")
            Array[index] -= 1
        return(all(x==0 for x in Array))
                
        