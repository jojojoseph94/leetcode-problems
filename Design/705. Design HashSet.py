"""
Using  double hashing to implement hashset.
To choose hashset double hash functions
If Range of elements to be inserted is known then 
Hash function1 -> key%Sqrt(MAX_NUM)
Hash function2 -> key/Sqrt(MAX_NUM)

This way collision will not occur in hash function2.

First initialize boolean array with size Sqrt(MAX_NUM)
Then whenever a key needs to be added, apply hashfunction1, check if the boolean value at that place
is True, if it is then apply hashfunction2 and set True at corresponding index.
If it is False, then create an array of Sqrt(MAX_NUM) at position after applying hashfunction1,
then apply hashfunction2 and add value
Space Complexity - O(N)
Time complexity - O(1)
"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.bucketItems = 1000
        self.storage = [False]*self.buckets
        
    # first hash function
    def bucket(self, key):
        return key%self.buckets

    #second hash function
    def bucketItem(self, key):
        return key/self.bucketItems
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        if not self.storage[bucket]:
            self.storage[bucket] = [False]*self.bucketItems
        self.storage[bucket][bucketItem] = True
            
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        if self.storage[bucket]:
            self.storage[bucket][bucketItem] = False
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket = self.bucket(key)
        bucketItem = self.bucketItem(key)
        if self.storage[bucket]:
            if self.storage[bucket][bucketItem]:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)