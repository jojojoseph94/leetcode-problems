"""
Bruteforce soln : For each possible continuos subarray, find sum and if sum is equal to target,
                  increase count
Time complexity : O(n^2) -> Two loops, building sum for each possible continuos subarray
Space complexity : O(1)
Leetcode timelimit exceeded
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(0,len(nums)):
            running_sum = 0
            for j in range(i,len(nums)):
                running_sum+=nums[j]
                if running_sum == k:
                    count+=1
        return count
        

"""
Optimized soln : 
At bruteforce soln, we are resetting the running sum at each iteration of outer loop. 
We can optimize that by saving the sum at each element, along with the number of times
the sum occured using a hashmap using hashmap.
Initialize the hashmap with {0:1}
At each point, calculate running sum - k and check if it is there in hashmap.
If it is, add the count by the corresponding entry in in the hashmap.
Then for each element, store running sum in a hashmap. 
NOTE : Need to understand logic better

Time complexity : O(N) since we iterate over the array once
Space complexity : O(N) since we store running sum at each point, worst case can be O(N)
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sum = 0
        count = 0
        hash_m = {0:1}
        for i in range(0,len(nums)):
            running_sum+=nums[i]
            if running_sum - k in hash_m:
                count+= hash_m[running_sum - k]
            if running_sum in hash_m:
                hash_m[running_sum]+=1
            else:
                hash_m[running_sum]=1
        return count
        