class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1
        # sortedmap = dict(sorted(hashmap.items(), key=lambda x:x[1], reverse=True))
        # result = list(sortedmap.keys())
        # return result[:k]
        
        """
        1. count calculate with dictionary
        2. populate array with count
        3. return k while iterating in descending
        """
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]: #because there can be multiple high values need to be kept in sub array for returning
                result.append(n)
                if(len(result) == k):
                    return result


            

        

            