"""
Bruteforce: Find all indices for the first alphabet of B in A.
            Then for all indexes in indices,
            check if B to end matches with A[index]->A[len(A)]->A[0]->A[index-1]
Time complexity : Finding indexes O(N)
                  Checking for match O(N)
Space complexity : O(N)-> Storing the indexes
"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        if len(A) == 0:
            return True
        indices = [i for i, x in enumerate(A) if x == B[0]]
        #iterate to see
        for index in indices:
            j = 0
            flag = True
            k = 0
            for i in xrange(index,len(A)):
                #print B[j],A[i],j,i
                k=i
                if B[j]!=A[i]:
                    flag = False
                    break
                j+=1
            #print flag,j,k
            if flag and j!=len(B):
                for i in xrange(0,k-j+1):
                    #print B[j],A[i],j,i
                    if B[j]!=A[i]:
                        flag = False
                        break
                    j+=1
            if j==len(B):
                return True
        return False