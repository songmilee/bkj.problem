class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = list()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
            self.hash_set.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        if self.contains(key):
            self.hash_set.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """

        if key in self.hash_set:
            return True
        
        return False
        
if __name__ == "__main__":
    hashSet = MyHashSet();
    hashSet.add(1);         
    hashSet.add(2);         
    hashSet.contains(1);    #// returns true
    hashSet.contains(3);    #// returns false (not found)
    hashSet.add(2);          
    hashSet.contains(2);    #// returns true
    hashSet.remove(2);          
    hashSet.contains(2);    #// returns false (already removed)