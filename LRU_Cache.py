"""
The efficiency of the code is following:
1. get : O(1)
2. set : O(1)

Design Choice:
1. Used a linked list to keep track of the most using items.
2. Used a fixed sized array to keep track of all nodes in the linked list.
3. The data is stored in a Map object
4. The Map object has the value and the array index. 

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        
        # Key is the key
        # value is a tuple of value and index of the index array
        self.hm = dict()
        
        # Head of the LL
        # Most used value
        self.head = None
        
        # Tail in the LL
        # Least used object
        self.tail = None
        # Fixed sized array to store the nodes
        self.index = [None for _ in range(capacity)]
        
        # Tracking current Size
        self.current_capacity = 0
        
        # Tracking current index
        self.current_pointer = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hm:
            
            # Get the value and pointer from the Map
            value, pointer = self.hm[key]
            
            # Retrieve the node from the array
            node = self.index[pointer]
            
            # Move the node at the begining of the Linked List
            if node.left is not None:
                node.left.right = node.right
            if node.right is not None:
                node.right.left = node.left
            
            if node.right is None:
                self.tail = node.left
                self.tail.right = None
                
            temp_node = self.head
            node.left = None
            temp_node.left = node
            node.right = temp_node
            self.head = node

            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.hm:
            
            # if the key is already present, just update the value
            # Call get() function first so that the node moves at the 
            # beginning of the LL
            value = self.get(key)

            _, pointer = self.hm[key]
            self.hm[key] = (value, pointer)

        # if the size < capacity
        elif self.current_capacity < self.capacity:
            
            # Create a new node
            new_node = Node(key)
            
            # Add the node at the beginning of the LL
            if self.head is None:
                self.head = new_node
                self.tail = self.head
            else:
                node = self.head
                new_node.right = node
                node.left = new_node
                self.head = new_node

                if node.right is None:
                    self.tail = node
            
            # Save the node in the array
            self.index[self.current_pointer] = new_node
            
            # Save the value and index of the array in the Map object
            self.hm[key] = (value, self.current_pointer)
            
            # Increase current size and pointer
            self.current_capacity += 1
            self.current_pointer += 1
        else:
            
            # If the LRU is at full capacity
            # Find the tail of the LL, which needs to be deleted
            
            key_to_be_deleted = self.tail.value
            self.tail = self.tail.left
            self.tail.right = None
            
            _, pointer = self.hm[key_to_be_deleted]
            
            # Remove the data from the Map
            del self.hm[key_to_be_deleted]
            
            # Create a new Node
            new_node = Node(key )
            
            # Save the node at the beginning
            node = self.head
            new_node.right = node
            node.left = new_node
            self.head = new_node
            
            # Save the value and index of the array in the Map object
            self.index[pointer] = new_node
            self.hm[key] = (value, pointer)


if __name__ == "__main__":
    # Test Cases
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(6))  # returns 1

    print(our_cache.get(3))  # returns -1
