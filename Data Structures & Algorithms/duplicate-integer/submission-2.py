class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        PastNum={} #stores visited numbers
        for i in nums:
            if i in PastNum:
                return (True)
            PastNum[i]=1
        return(False)
        