class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        k = -1

        for _ in range(len(nums)//2):
            min_sum += min(nums[k], nums[k-1])
            k -= 2
        return min_sum
