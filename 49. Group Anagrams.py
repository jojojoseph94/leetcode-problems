"""
Bruteforce soln 1 : exponential complexity
                    for every word in list, create all possible anagrams using backtracking..
                    and check for each anagram in answer
Brute force soln 2 : O(n^2)
                    for every word in given list, check if anagram(word,word2) for every word2 in ans
                    Leetcode Timelimit exceeded
Optimized soln 3 : O(NxMlog(M)): For every word, sort it. Then check if it is in ans dictionary
                    Sorting takes Mlog(M) and you have to do the same for N words in the given input

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def is_anagram(worda, wordb):
            count_a = [0]*26
            count_b = [0]*26
            for i in worda:
                count_a[ord(i) - ord('a')]+=1
            for i in wordb:
                count_b[ord(i) - ord('a')]+=1
            return count_a == count_b 
        # soln 1 brute force O(n^2)
        ans = []
        for word1 in strs:
            index = -1
            index2 = 0
            for words in ans:
                char1 = 0
                if index!=-1:
                    break
                for word2 in words:
                    flag = is_anagram(word1,word2)
                    if flag:
                        ans[index2].append(word1)
                        index = index2
                        break
                    else:
                        index2+=1
                        break
            if index == -1:
                ans.append([str(word1)])
        return ans

"""
Optimized soln : O(NxMlog(M)): For every word, sort it. Then check if it is in ans dictionary
                    Sorting takes Mlog(M) and you have to do the same for N words in the given input

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # soln 2 optimized
        ans = {}
        for word1 in strs:
            word_s = str(sorted(word1))
            if word_s in ans:
                ans[word_s].append(word1)
            else:
                ans[word_s] = [word1]
        ret = []
        for key in ans.keys():
            ret.append(ans[key])
        return ret       