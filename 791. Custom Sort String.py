"""
Bruteforce soln : First for every char in S, check if it occurs in T. If yes add it to ans
                  Keep tab of chars not in S
                  Finally for every char not in S, check if it occurs in T. 
                  If yes add it to ans.

Time complexity : O(26*N) + O(26*N) 
Space complexity : O(N)
Leetcode Accepted : Yes
"""

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        ans = ""
        others = [1]*26
        for i in range(0, len(S)):
            this_s = ""
            for j in range(0,len(T)):
                if T[j] == S[i]:
                    this_s+=T[j]
            ans+=this_s
            others[ord(S[i]) - ord('a')] = 0
        for i in range(0,len(others)):
            if others[i] == 1:
                for j in range(0,len(T)):
                    if i == (ord(T[j]) - ord('a')):
                        ans+=T[j]
        #print ans
        return ans
        