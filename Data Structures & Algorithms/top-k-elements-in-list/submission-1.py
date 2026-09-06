import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Tracker={}
        for i in nums:
            Tracker[i]= 1 + Tracker.get(i,0)
        value_key_pairs = [(v, k) for k, v in Tracker.items()]
        Largest_value_key_pairs=h.nlargest(k, value_key_pairs)
        Keys=[key for val, key in Largest_value_key_pairs]
        return(Keys)

        