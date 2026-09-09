class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        longest=1
        current=1
        order=sorted(list(set(nums)))
        for i in range(len(order)-1):
            if order[i+1]-order[i]==1:
                current+=1
                longest=max(longest,current)
                continue
            current=1
        return longest
        -1,0,1,3,4,5,6,7,8,9