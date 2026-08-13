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

        