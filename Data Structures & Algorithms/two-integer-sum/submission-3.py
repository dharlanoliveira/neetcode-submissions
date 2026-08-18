class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort()

        left = 0
        right = len(indexed) - 1

        while left < right:
            total = indexed[left][0] + indexed[right][0]

            if total == target:
                i = indexed[left][1]
                j = indexed[right][1]

                return [min(i, j), max(i, j)]

            elif total < target:
                left += 1
            else:
                right -= 1

        return []