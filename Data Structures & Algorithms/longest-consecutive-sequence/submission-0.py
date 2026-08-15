class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 in numset:
                continue
            else:
                start = nums[i]
                counter = 0
                while start in numset:
                    counter = counter + 1
                    start = start + 1
                if counter > longest:
                    longest = counter        
        return longest

