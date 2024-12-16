from heapq import heappop, heappush
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        pq = []
        for i, num in enumerate(nums):
            heappush(pq, (num, i))
        while k > 0:
            k -= 1
            val, idx = heappop(pq)

            nums[idx] = val * multiplier
            heappush(pq, (nums[idx], idx))

        return nums