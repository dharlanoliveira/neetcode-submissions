class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        current_number = -1000
        current_sequence = 0
        longest_sequence = -1000

        nums_sorted = sorted(set(nums))

        for num in nums_sorted:
            if num == current_number + 1:
                current_sequence += 1
            else:
                current_sequence = 1

            current_number = num

            if current_sequence > longest_sequence:
                longest_sequence = current_sequence

        return longest_sequence       

