"""
Bruteforce solution : Check for every possible word change possible. 
                      This way we check all possible paths.
Time Complexity : Exponential (??), Since its exploring all possible paths to answer
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        answer = []
        def helper(beginWord, endWord, wordList, count):
            #if endWord not in wordList:
            #    answer.append(999)
            #    return 999
            if beginWord == endWord:
                #print "Here 1"
                return count
            if wordList == []:
                #print "Here 2"
                return 999
            for word in wordList:
                count_ = 0
                candidate = True
                for i in range(0,len(word)):
                    if word[i] != beginWord[i]:
                        count_+=1
                    if count_ > 1:
                        candidate = False
                        break
                if candidate and count_ == 1:
                    #print "Candidate ", candidate
                    newWords = wordList[0:wordList.index(word)] + wordList[wordList.index(word)+1:]
                    answer.append(helper(word, endWord, newWords, count+1))
            return 999 
        
        helper(beginWord, endWord, wordList, 1)
        if answer == []:
            return 0
        min_ = answer[0]
        print answer
        for i in xrange(1,len(answer)):
            min_ = min(min_, answer[i])
        if min_ == 999:
            return 0
        return min_

"""
BFS solution : Do breadth first search for each word variation
Time complexity : O(M*N) -> M = length of word, N number of words
Space complexity : O(M*N) -> queue with max size M*N
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def one_dist(word):
            pattern = []
            for i in range(0,len(word)):
                pattern.append(word[0:i] + "*" + word[i+1:])
            return pattern

        answer = 0
        queue = [[beginWord, 1]]
        visited = {}
        one_distance = {}
        
        for i in range(0,len(wordList)):
            for w in one_dist(wordList[i]):
                if w not in one_distance:
                    one_distance[w] = [wordList[i]]
                else:
                    one_distance[w].append(wordList[i])
        while queue:
            begin, depth = queue.pop(0)
            #print begin, depth
            if begin not in visited:
                visited[begin] = True
                for word in one_dist(begin):
                    #print word
                    if word in one_distance:
                        for w in one_distance[word]:
                            if w == endWord:
                                return depth+1
                            if w not in visited:
                                #visited[word] = True
                                #print queue, word, depth+1
                                queue.append([w, depth+1])
        return answer