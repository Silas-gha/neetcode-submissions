class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        PastNum={} #stores visited numbers
        for i in nums:
            if i in PastNum:
                return (True)
            else:
                PastNum[i]=1
        return(False)
        