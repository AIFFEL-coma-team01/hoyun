class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        temp = []
        for i in range(len(nums)-1):
            left = nums[:i]
            right = nums[i+1:]
            prod_list = left+right
            temp.append(math.prod(prod_list))

        temp.append(math.prod(nums[:-1]))

        return temp
