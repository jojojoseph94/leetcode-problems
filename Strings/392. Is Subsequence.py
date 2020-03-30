"""
Logic : Create a hashmap of long string with entries char : [list of indexes]
        For each character in smaller string, if the char is not in map, return False
        If char is in hashmap, do binary search of the list of indexes to see if there 
        is a larger index than previous character in the list
        If its not there return False

Time Complexity : O(Nlog(N)) -> O(N) being length of smaller string and log(N) to perform binary search

Space Complexity : O(N) -> To store hashmap
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def binarySearch(ele, left, right, seq):
            while left<=right:
                mid = (left + right)/2
                if seq[mid] > ele:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(seq):
                return -1
            else:
                return seq[left]
        
        dict_ = {}
        for index, letter in enumerate(t):
            if letter in dict_:
                dict_[letter]+=[index]
            else:
                dict_[letter] = [index]
        prev = -1
        #print dict_
        for letter in s:
            if letter not in dict_:
                return False
            else:
                prev = binarySearch(prev, 0, len(dict_[letter]) -1, dict_[letter])
                if prev == -1:
                    return False
                #prev+=1
        return True