"""
Soln: For every element in matrix which is 1, check incrementally for squares of length 2,3,4,...
      For example at index [0,0] of the following matrix, the check happens in the following way
      | 1 1 1 |     | X 1 1 |    | 1 X 1 |    | 1 1 X |
      | 1 1 0 | ->  | 1 1 0 | -> | X X 0 | -> | 1 1 X |
      ! 1 1 0 |     | 1 1 0 |    | 1 1 0 |    | X X X | (X is the element being checked)
Time complexity : O((N*M)^2)
TODO Implement DP solution
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #brute force
        mx_sq_len = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == '1':
                    # check for squares
                    sq_len = 1
                    flag = True
                    while((len(matrix)>sq_len+i) and (len(matrix[i])>sq_len+j) and (flag)):
                        # check row
                        for m in range(i,sq_len+i+1):
                            if matrix[m][j+sq_len] == '0':
                                flag = False
                                break
                        if flag:
                            for n in range(j,sq_len+j+1):
                                if matrix[i+sq_len][n] == '0':
                                    flag = False
                                    break
                        if flag:
                            #print i,j
                            sq_len+=1
                    mx_sq_len = max(sq_len,mx_sq_len)
        return mx_sq_len*mx_sq_len