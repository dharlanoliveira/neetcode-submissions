import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        result = []
        
        for num in nums:
             result.append(self.count_sum(count,num))

        return result

    def count_sum(self,count: Dict,reference: int) -> int:
        result = 1
        for num,occur in count.items():
            if(num == reference):
                result *= pow(num,occur - 1)            
            else:
                result *= pow(num,occur)   
        return result                             
            

        