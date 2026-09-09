class Solution:

    def encode(self, strs: List[str]) -> str:
        for index, string in enumerate(strs):
            strs[index]=str(len(string))+"#"+string
        encoded_string="".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        Output=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            Output.append(s[j+1:j+1+length])
            i=j+1+length
        return Output
             

