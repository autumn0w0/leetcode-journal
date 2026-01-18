class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = maxlen =0
        usedchar = {}

        for i in range (len(s)):
            if s[i] in usedchar and start <= usedchar[s[i]]:
                start = usedchar[s[i]] + 1
            else:
                maxlen = max(maxlen,i - start + 1)

            usedchar[s[i]] = i

        return maxlen       