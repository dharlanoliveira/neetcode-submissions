class Solution:

    def countChars(self, str1: str):
        count: Dict[str, int] = {}

        for char in str1:
            count[char] = count.get(char, 0) + 1

        return tuple(sorted(count.items()))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for i,str1 in enumerate(strs): 
            count = self.countChars(str1)

            if count not in groups:
                groups[count] = [str1]
            else:
                groups[count].append(str1)    

        return list(groups.values())

   