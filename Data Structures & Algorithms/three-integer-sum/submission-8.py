class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i, val in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue

            j, k= i+1, len(nums)-1

            while j<k:
                target=-(val)
                if nums[j]+nums[k]<target:
                    j+=1
                elif nums[j]+nums[k]>target:
                    k-=1
                else:
                    res.append([val,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

        return res
