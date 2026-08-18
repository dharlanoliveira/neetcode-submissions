class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            if(i + 1 > len(nums)):
                continue

            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        return []