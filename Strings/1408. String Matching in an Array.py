"""
Bruteforce soln: For every word, iterate over every other word with length less than it
                 To check if its a substring of the given word, 
                 Iterate over every alphabet on both
Time complexity : O(N^2*S) where N is number of words and S in length of the word
"""
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = {}
        for i in xrange(0,len(words)):
            for j in xrange(0,len(words)):
                if i!=j and len(words[i]) <= len(words[j]):
                    k = 0
                    l = 0
                    while 1:
                        if k >= len(words[i]):
                            #print "Here ", words[i], words[j]
                            ans[words[i]] = 0
                            break
                        if l>=len(words[j]):
                            break
                        #print words[i], words[j],k,l, ans
                        if words[i][k] == words[j][l]:
                            k+=1
                            l+=1
                        else:
                            if not k:
                                k=0
                                l+=1
                            else:
                                l-=k
                                l+=1
                                k=0
        return ans.keys()
                         