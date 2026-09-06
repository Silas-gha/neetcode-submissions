class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Dictionary that maps charCount to list of anagrams 
        CountKey=defaultdict(list)

        for i in strs:
            Counter=[0]*26

            for c in i:
                Counter[ord(c)-ord("a")]+=1

            CountKey[tuple(Counter)].append(i)   

        return list(CountKey.values())

        