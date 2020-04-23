"""
Bruteforce : For a given string, iterate over the indexes, taking the index as the middle point 
             of the palindrome. From the middle point, check if left and right 
Time complexity : O(n^2)
Space complexity : O(1)

Other approaches: 


"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s,i,j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        
        ans = ""
        for i in xrange(0,len(s)):
            str_ = helper(s,i,i)
            if len(str_) > len(ans):
                ans = str_
            str_ = helper(s,i,i+1)
            if len(str_) > len(ans):
                ans = str_
        return ans
                        