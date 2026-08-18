class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i,number in enumerate(nums):
            count[number] = count.get(number, 0) + 1
        sorted_count = sorted(count.items(), key=lambda item: item[1],reverse=True)[:k]
        return [key for key, value in sorted_count]

        