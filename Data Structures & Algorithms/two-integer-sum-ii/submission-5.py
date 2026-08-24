class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_with_index = sorted(enumerate(nums), key=lambda x: x[1])

        left = 0
        right = len(nums_with_index) - 1

        while left < right:
            left_index, left_value = nums_with_index[left]
            right_index, right_value = nums_with_index[right]

            current_sum = left_value + right_value

            if current_sum == target:
                return [left_index + 1, right_index + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1

        return []