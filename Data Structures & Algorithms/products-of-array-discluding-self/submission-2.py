class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        prefix=[nums[0]]*len(nums)
        suffix=[nums[len(nums)-1]]*len(nums)
        left=1
        right=len(nums)-2

        while left<len(nums) and right >= 0:
            prefix[left]=(nums[left]*prefix[left-1])
            suffix[right]=(nums[right]*suffix[right+1])
            left+=1
            right-=1
        
        for i in range(len(nums)):
            if i==0:
                output[i]=suffix[1]
                continue
            if i==len(nums)-1:
                output[i]=prefix[len(output)-2]
                continue
            output[i]=prefix[i-1]*suffix[i+1]

        return output


        