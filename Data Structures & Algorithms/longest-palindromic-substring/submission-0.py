class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        r=len(s)-1

        start=0
        length=0

        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>length:
                    start=l
                    length=r-l+1
                l-=1
                r+=1

            l=i
            r=i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>length:
                    start=l
                    length=r-l+1

                l-=1
                r+=1
        return s[start:length+start]