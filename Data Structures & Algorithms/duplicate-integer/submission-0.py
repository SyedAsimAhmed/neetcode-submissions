class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     # print(nums[i])
        #     count = nums.count(nums[i])
        #     if count > 1:
        #         return True
        # return False
        # dict = {}


        # s = set()
        # for i in range(len(nums)):
        #     if(nums[i] in s):
        #         return True
        #     else:
        #         s.add(nums[i])
        # return False


        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False