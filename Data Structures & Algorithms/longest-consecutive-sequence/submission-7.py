class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0

        Unique=defaultdict(int)

        for i in nums:
            Unique[i]+=1
        
        longest=1
        current=1
        for i in nums:
            if i-1 not in Unique:
                val=i
                while val+1 in Unique:
                    current+=1
                    longest=max(longest,current)
                    val+=1
                current=1
        
        return longest
                    
                

