class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Output=[]
        Ordered=sorted(nums)

        for i in range(len(Ordered)):
            target=-(Ordered[i])
            j=i+1
            k=len(Ordered)-1

            while j<k:
                if Ordered[j]+Ordered[k]==target:
                    Temp=sorted([Ordered[i],Ordered[j],Ordered[k]])
                    if Temp not in Output:
                        Output.append(Temp)
                    j+=1
                    k-=1
                if Ordered[j]+Ordered[k]<target:
                    j+=1
                    continue
                if Ordered[j]+Ordered[k]>target:
                    k-=1
                    continue
        return Output

