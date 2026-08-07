class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        
        # hash_map = {}
        # for i in range(len(nums)):
        #     if target-nums[i] in hash_map:
        #         return [hash_map[target-nums[i]], i]
        #     else:
        #         hash_map[nums[i]] = i

        hash_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[n] = i