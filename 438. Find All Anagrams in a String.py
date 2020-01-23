"""
Algorithm : Keep one counter with p.
            for each char in s -> check if it is in p_counter
            if it is decrement the corresponding count by one, remove it if the count reaches zero
                now if p_counter is empty, then add i - len(p)+1 to result
            if char is s is not in p_counter, then check if it is the same character as first char in window
            if it is not, then reset counter and decrement count if it is there in p

Timecomplexity : O(N)
Space complexity : O(1), since number of alphabets are constant

"""

from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_counter = Counter(p)
        
        for i in range(0,len(s)):
            if s[i] in p_counter:
                p_counter[s[i]]-=1
                if p_counter[s[i]] == 0:
                    p_counter.pop(s[i])
                if p_counter == Counter():
                    res.append(i-len(p)+1)
                    p_counter[s[i-len(p)+1]]=1
            else:
                if s[i-len(p)+1] != s[i]:
                    p_counter = Counter(p)
                    if p_counter[s[i]]:
                        p_counter[s[i]]-=1
                        if p_counter[s[i]] == 0:
                            p_counter.pop(s[i])
        return res
                
                
        