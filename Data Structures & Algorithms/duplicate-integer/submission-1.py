class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        PastNum=set() #stores visited numbers
        for i in nums:
            if i in PastNum:
                return (True)
            PastNum.add(i)
        return(False)
        