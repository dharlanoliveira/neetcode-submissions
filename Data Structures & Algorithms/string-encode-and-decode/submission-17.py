class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0): return "0:::"
        if(len(strs) == 1): return "1:::" + strs[0]
        return str(len(strs)) + ":::" + "---".join(strs)

    def decode(self, s: str) -> List[str]:        
        str_number, rest = s.split(":::", 1)
        number = int(str_number)
        if(number == 0): return []
        if(number == 1): return [rest]
        else: return rest.split("---")