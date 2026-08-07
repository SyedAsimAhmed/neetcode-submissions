class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for i in set(s):
            dicts[i] = s.count(i)
        for j in set(t):
            dictt[j] = t.count(j)

        print(dicts, dictt)
        if (dicts == dictt):
            return True
        else:
            return False
        
        # sorteds = sorted(s)
        # sortedt = sorted(t)
        # if sorteds == sortedt:
        #     return True
        # else:
        #     return False
