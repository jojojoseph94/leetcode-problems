"""
    Sort strings. Check each char in t with s.
    Time complexity : O(Nlog(N) + Nlog(N) + N)
    Space complexity : O(1)

"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(0,len(t)-1):
            if t[i] != s[i]:
                return t[i]
        return t[len(t)-1]

"""
Use a hashmap for chars in s. for each char in t, see if its there in hashmap
if yes decrement the count. if count becomes zero, remove from hashmap
if not return the char
Time complexity : O(N)
Space complexity : O(N)
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1
        for j in t:
            if j in s_dict:
                s_dict[j]-=1
                if s_dict[j] == 0:
                    del s_dict[j]
            else:
                return j
        
        