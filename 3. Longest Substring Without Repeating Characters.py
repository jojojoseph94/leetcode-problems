"""
My Solution : For every character in string, start from the character
              and check if it is unique. If its not break and start with next character

Time complexity : O(n^2)
Space complexity : O(n)
Leetcode Accepted : yes
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ = 0
        i = 0
        while(i < len(s)):
            dic_ = {}
            dic_[s[i]] = True
            len_ = 1
            k=i+1
            while (k < len(s)):
                if s[k] in dic_:
                    break
                else:
                    len_+=1
                    dic_[s[k]] = True
                    k+=1
            i+=1
            max_ = max(max_, len_)
        return max_
        

"""
My solution 2 : sliding window; Keep a sliding window, with it length and doctionary with
                characters in the window with indexes stored.
                When a new character comes, check if it is there in the dict. 
                If it isn't add to dict and increment length and stuff.
                If it is, slide the window to the location after the previous occurance 
                of that character in the window, update the length as well
Time complexity : O(N)
Space complexity : O(N)
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ = 0
        i = 0
        k = 0
        len_ = 0
        dic_ = {}
        while i < len(s) and k < len(s):
            #print len_,i,k,s[i:k], dic_
            if s[k] in dic_:
                # remove every letter before window?
                for j in range(i,dic_[s[k]]):
                    if s[j] != s[k]:
                        del dic_[s[j]]
                i = dic_[s[k]]+1
                len_ = k - i +1
                dic_[s[k]] = k
                k+=1
            else:
                dic_[s[k]] = k
                k+=1
                len_+=1
            max_ = max(max_, len_)
        return max_
        