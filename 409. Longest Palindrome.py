"""
For every alphabet (52) in case of upper case too, I increment corresponding count.
If count becomes two for an alphabet, 
reset it to zero and add it to ans
Finally if ans is even, check for an alphabet with count set to 1 and add it to ans 
Complexity : O(N)

This can also be done using hashset too. 
Add an element to hashset if it doesn't exist. If it exists, remove it from hashset and add 2 to the ans.
Finally if ans is even, add 1 to ans if hashset is nonempty.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        s_set = [0]*52
        for alpha in s:
            if ord(alpha) <= ord('z'):
                index = ord('a')
            else:
                index = ord('A') + 25
            if s_set[ord(alpha) - index] == 0:
                s_set[ord(alpha) - index]+=1
            else:
                s_set[ord(alpha) - index]+=1
                if s_set[ord(alpha) - index] == 2:
                    ans+=2
                    s_set[ord(alpha) - index] = 0
        if ans%2 == 0:
            for i in range(0,26):
                if s_set[i] == 1:
                    ans+=1
                    break
        return ans
        