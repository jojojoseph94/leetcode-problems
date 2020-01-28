"""
Bruteforce : sort the numbers , starting from last do operation as required
TIme complexity : (O(NlogN))
Space complexity : O(N)
"""
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones)
        #print len(stones)-1, 0
        i = len(stones)-1
        while i > 0:
            #print i, "in loop"
            #print stones
            if stones and len(stones) > 1:
                new_x = stones[i] - stones[i-1]
                if new_x == 0:
                    stones.pop(-1)
                    stones.pop(-1)
                    i-=1
                else:
                    if i-1 >= 0:
                        stones = sorted(stones[:i-1] + [new_x])
                    else:
                        stones = [new_x]
                        break
                i-=1
        if stones:
            return stones[0]
        else:
            return 0


"""
 Logic : Sort the numbers into buckets. Then from highest number work backwards
        if number is even, it cancels out
        if number is odd, find a smaller number and remove both numbers
         and bucket[num1 - num2]+=1
 Time complexity : O(N); worst complexity while searching for 2 numbers could be 1000*1000 -> O(1)
 Space complexty : O(1) -> number is from 0 to 1000
"""
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # bucket sort
        bucket = [0]*1000
        for stone in stones:
            bucket[stone]+=1
        #prev = None
        highest = None
        for i in range(999, 0, -1):
            if bucket[i]!=0 and bucket[i]%2!=0:
                #print "At node ", i
                highest = i
                bucket[i]=1
                this = None
                for j in range(i-1,-1,-1):
                    if bucket[j]!=0:
                        this = j
                        break
                if this:
                    #print "Processing ",i,j 
                    bucket[j]-=1
                    bucket[i-j]+=1
                    bucket[i]=0
            elif bucket[i]%2 == 0:
                bucket[i] = 0
        for i in range(999,-1,-1):
            if bucket[i]!=0:
                return i
        return 0
                        
                    