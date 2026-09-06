class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map={}
        for i, Val_i in enumerate(nums):
            x=target-Val_i
            if x in Map:
                return([Map[x],i])
            else:
                Map[Val_i]=i
        

            

        