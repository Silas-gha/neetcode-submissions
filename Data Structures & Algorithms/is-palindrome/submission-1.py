class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned="".join(c for c in s if c.isalnum()).lower()
        LeftPointer=0
        RightPointer=len(cleaned)-1
        while RightPointer>LeftPointer:
                if cleaned[RightPointer] != cleaned[LeftPointer]:
                    return False
                LeftPointer+=1
                RightPointer-=1
        return True

