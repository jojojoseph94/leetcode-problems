"""
Soln: Convert m and n to binary
      If number of bits are not equal, return 0
      For a bit in n which is 1, if the corresponding bit in m in 0, 
      it means that every lower bit will have to change in between m and n.
      So break
      And to the answer add that many bits of zero.
Time complexity : O(N)
Space complexiy : O(N)  
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        b1 = bin(m).replace("0b","")
        b2 = bin(n).replace("0b","")
        if len(b1) < len(b2):
            return 0
        ans = ""
        index = -1
        for i in range(0,len(b2)):
            if b1[i] == "0" and b2[i] == "1":
                index = i
                break
            else:
                ans+=b2[i]
        if index!=-1:
            ans+=("0"*(len(b2)-index))
        return int(ans,2)