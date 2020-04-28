"""
Soln: hashmap to store actual key value pairs.
      list to store the keys based on last access
      the end of the list will contain the most accessed keys
      If a key is put, if it is not in the list, it is appended to the end of the list
      else, the key taken from its current position to the end of the list
      If a key is get, if succesful, it is moved from current postion to end of the list, if its already
      in the list. Else it is simply appended to the end.

Time complexity : O(N) get
                  O(N) put -> 

To optimize and reach O(1), use a linked list with hashmap
before hashmap, which stores key accessed before, and after hashmap which stores key accessed after.
Also keep tail and head for accessing the key most accessed and least accessed keys
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.stack = []
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            #do stack operation
            #if key in stack, pop
            index = -1
            for k in range(0,len(self.stack)):
                if self.stack[k] == key:
                    index = k
                    break
            if index!=-1:
                self.stack.pop(index)
            # put on top
            self.stack.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #check if same key
        if key in self.cache:
            #update key
            self.cache[key] = value
            # bring to top of stack
            index = -1
            for k in range(0,len(self.stack)):
                if self.stack[k] == key:
                    index = k
                    break
            if index!=-1:
                self.stack.pop(index)
            # put on top
            self.stack.append(key)
        else:
            if self.size < self.capacity:
                self.cache[key] = value
                self.size+=1
                # on top of stack
                self.stack.append(key)
            else:
                #evict one
                k = self.stack.pop(0)
                del self.cache[k]
                #put one
                self.cache[key] = value
                self.stack.append(key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)