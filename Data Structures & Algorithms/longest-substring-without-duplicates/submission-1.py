class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new=set()
        l=0
        maxlen=0

        for r in range(len(s)):
                while s[r] in new:
                    new.remove(s[l])
                    l+=1
                new.add(s[r])
                maxlen=max(maxlen,r-l+1)
        return maxlen
