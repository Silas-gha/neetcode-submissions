import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Tracker={}
        Bucket=[[] for _ in range(len(nums)+1)]
        for i in nums:
            Tracker[i]= 1 + Tracker.get(i,0)

        Value_Key_Pairs=[(Val, key) for key, Val in Tracker.items()]

        for  Val, Key in Value_Key_Pairs:
            Bucket[Val].append(Key)

        Output=[]
        for i in range(len(Bucket)-1, 0, -1):
            if Bucket[i]  and len(Output)<k:
                Output.extend(Bucket[i])
        return(Output)
        
        
        
        
        