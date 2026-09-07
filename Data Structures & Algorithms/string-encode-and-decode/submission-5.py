class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[]:
            return "x1f"
        JoinedString="\x1f".join(strs)
        chars=list(JoinedString)
        for i in range(0, len(chars)-1, 2):
            chars[i], chars[i+1]=chars[i+1], chars[i]
        JoinedString="".join(chars)
        return JoinedString



    def decode(self, s: str) -> List[str]:
        if s=="x1f":
            return []
        chars=list(s)
        for i in range(0, len(chars)-1, 2):
            chars[i], chars[i+1]=chars[i+1], chars[i]
        s="".join(chars)
        result=s.split("\x1f")
        
        return result

