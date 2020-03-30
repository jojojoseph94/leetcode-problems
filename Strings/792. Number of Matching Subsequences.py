"""
Logic : Similar to 392. First hashmap of characters along wiht index in S is created.
        Then for each word in words,
            for each char in word,
                if char is not in map, its not subsequence
                if char is there, do binary search starting with prev -1 for index greater than prev 
        Return total number of subsequences

Time Complexity : O(N*log(N)*(M)) -> N length of word, M number of words
Space complexity : O(N), where N is the length of longer string
More efficient soln below
"""
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # top level hashset to avoid duplicates
        notsubs = {}
        subs = {}
        # to check if subsequence
        def isSubseq(word, hashmap):
            if word in notsubs:
                return False
            if word in subs:
                return True
            prev = -1
            for char in word:
                if char not in hashmap:
                    notsubs[word] = True
                    return False
                prev = binarySearch(prev, 0, len(hashmap[char])-1, hashmap[char])
                if prev == -1:
                    notsubs[word] = True
                    return False
            subs[word] = True
            return True
        # for binary search
        def binarySearch(ele, left, right, seq):
            while (left <= right):
                mid = (left+right)/2
                if seq[mid] > ele:
                    right = mid -1
                else:
                    left = mid +1
            if left == len(seq):
                return -1
            return seq[left]
        # main
        dict_ = {}
        for index,char in enumerate(S):
            if char in dict_:
                dict_[char]+=[index]
            else:
                dict_[char] = [index]
                
        ans = 0
        for word in words:
            if isSubseq(word, dict_):
                ans+=1
        return ans

"""
Logic: Similar to Tries
        Starting with first character of strings to be checked, we keep hashmap with 
        index and full word.
        Then for each character in long string, if it is in map, remove the entries,
         check for each entry in map
            -> see if the index is equal to length of word; if yes result+=1; remove from list
            -> Append index+1, word to corresponding map entry (word[index+1])
Time Complexity : O(N*M) -> N length of word and M number of words
Space Complexity : O(N*M) -> N length of word and M number of words
"""

class Solution(object):
    def numMatchingSubseq(self, S, words):
        needs = {}
        for word in words:
            if word[0] in needs:
                needs[word[0]].append([0, word])
            else:
                needs[word[0]] = [[0, word]]
        matches = 0
        for c in S:
            if c in needs:
                met_needs = needs[c]
            else:
                met_needs = []
            needs[c] = []
            for i, w in met_needs:
                if i+1 >= len(w):
                    matches += 1
                    continue
                if w[i+1] in needs:
                    needs[w[i+1]].append([i+1, w])
                else:
                    needs[w[i+1]] = [[i+1, w]]
        return matches