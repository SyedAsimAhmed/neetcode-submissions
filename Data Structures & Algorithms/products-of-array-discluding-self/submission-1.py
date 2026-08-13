class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [0 for i in range(l)]
        suffix = [0 for i in range(l)]
        result = []
        prefix[0] = 1
        suffix[l - 1] = 1
        for i in range(1, l):
            prefix[i] = nums[i - 1] * prefix[i-1]
        for j in range(l-2, -1 , -1):
            suffix[j] = nums[j+1] * suffix[j+1]
        for i in range(l):
            result.append(prefix[i] * suffix[i])
        return result

        #optimal solution below
        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res