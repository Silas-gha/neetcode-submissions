class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Key=defaultdict(list)



        for i in strs:
            Counter=[0]*26
            for c in i:
                Counter[ord(c)-ord("a")]+=1
            Key[tuple(Counter)].append(i)

        return list(Key.values())