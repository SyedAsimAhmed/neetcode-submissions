class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash_map = {}
        # for n in strs:
        #     sorted_value = ''.join(sorted(n))
        #     if sorted_value in hash_map:
        #         hash_map[sorted_value].append(n)
        #     else:
        #         hash_map[sorted_value] = [n]
        # return list(hash_map.values())

        hashmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s) 
        return list(hashmap.values())
        
