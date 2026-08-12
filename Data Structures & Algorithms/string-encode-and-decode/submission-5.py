class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ''
        for string in strs:
            encodedstr = encodedstr + str(len(string)) + '#' + string
        print(encodedstr)
        return encodedstr

    # def decode(self, s: str) -> List[str]:
    #     decoded_strs = []
    #     length = len(s)
    #     while length > 0:
    #         # count = int(s[0])
    #         index = s.find("#")
    #         print(index, s)
    #         count = int(s[:index])
    #         # intcount = int(count)
    #         limiter = s[index]
    #         print(count, limiter)
    #         print(type(count))
    #         # word = s[2:count + 2]
    #         word = s[index+1:count+index+1]
    #         decoded_strs.append(word)
    #         # s = s[count + 2:]
    #         s = s[count + index + 1:] 
    #         length = length - count - index - 1
    #     return decoded_strs
    def decode(self, s: str) -> List[str]:
        decoded_strs = []

        while s:
            index = s.find("#")
            count = int(s[:index])

            word = s[index + 1:index + 1 + count]
            decoded_strs.append(word)

            s = s[index + 1 + count:]

        return decoded_strs