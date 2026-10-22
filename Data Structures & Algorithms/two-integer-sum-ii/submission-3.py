class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(i, numbers, search):
            left=i+1
            right=len(numbers)-1
            while left <= right:
                midpoint=(left+right)//2
                if numbers[midpoint]==search:
                    return(midpoint)
                if search>numbers[midpoint]:
                    left=midpoint+1
                if search<numbers[midpoint]:
                    right=midpoint-1


            return -1
        
        for i in range(len(numbers)):
            search=target-numbers[i]
            if binary_search(i, numbers, search) == -1:
                continue
            return[i+1, binary_search(i, numbers, search)+1]


            