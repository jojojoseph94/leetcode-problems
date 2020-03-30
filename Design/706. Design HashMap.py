"""
Hashmap using chaining method
In case of collision of keys after hashing, chaining is used which involves
creating a linked list containing the elements one after the other
Here since hash function used in mod 10,000, the chains can be of length upto 100 nodes
Insert delete and get will all be done in constant time
"""

class MyHashMap(object):
    class Node(object):
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.next = None
        
    
    def __index__(self,key):
        return int(hash(key))%10000
    
    def __find(self,node, key):
        cur = node
        prev = None
        while cur:
            if cur.key == key:
                return prev
            else:
                prev = cur
                cur = cur.next
        return -1
            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = [None]*10000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.__index__(key)
        if self.nodes[index] == None:
            self.nodes[index] = self.Node(key,value)
            return
        prev = self.__find(self.nodes[index], key)
        if prev == -1:
            # create a new node at end of list
            # navigate to last
            cur = self.nodes[index]
            while (cur.next):
                cur = cur.next
            node = self.Node(key,value)
            cur.next = node
        elif prev == None:
            cur = self.nodes[index]
            cur.val = value
        else:
            cur = prev.next
            cur.val = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = self.__index__(key)
        if self.nodes[index] == None:
            return -1
        prev = self.__find(self.nodes[index], key)
        if prev == -1:
            return -1
        elif prev == None:
            return self.nodes[index].val
        else:
            return prev.next.val
            
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = self.__index__(key)
        if self.nodes[index] == None:
            return
        prev = self.__find(self.nodes[index], key)
        if prev == -1:
            return
        elif prev == None:
            self.nodes[index] = self.nodes[index].next 
        else:
            prev.next = prev.next.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)