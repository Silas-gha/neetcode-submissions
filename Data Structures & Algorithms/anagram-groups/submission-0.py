class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Dictionary that will store the sorted anagrams as keys 
        SortedKey={}

        for i in strs:
            SortedKey[''.join(sorted(i))]=[]
        for i in strs:
            if ''.join(sorted(i)) in SortedKey:
                SortedKey[''.join(sorted(i))].append(i)
        return(list(SortedKey.values()))
        

        

        