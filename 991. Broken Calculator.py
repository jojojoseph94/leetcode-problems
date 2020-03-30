"""
Broken calculator : Logic -> Working backwards
                             To reach Y from X,
                             we divide Y/2 until we reach less than X
                             but to keep dividing by 2, if the number is odd, we add by one
                             Finally when Y is less than X,
                             add X-Y to final answer

                eg : X : 5, Y: 8
                    to reach 5 from 8, I Calculate how to reach 8 from 5
                    I keep dividing 8
                    Y -> 8 -> 4
                    4<5 so comes out of loop
                    then ops = 1 + (5-4) = 2

                    which is the minimum number of operations to reach 8 from 5 sing xply and subtract
                    (5-1)*2

Timecomplexity : O(log(Y)) -> We keep dividing Y by 2 so log
Space complexity : O(1)

"""

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        ops = 0
        while Y>X:
            ops+=1
            if Y%2:
                Y+=1
            else:
                Y= Y/2
        return ops + X-Y
        
        