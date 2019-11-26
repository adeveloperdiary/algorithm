class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hm = dict()
        self.head = None
        self.tail = None
        self.index = [None for _ in range(capacity)]
        self.current_capacity = 0
        self.current_pointer = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.hm:

            value, pointer = self.hm[key]
            node = self.index[pointer]

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
            value = self.get(key)

            _, pointer = self.hm[key]
            self.hm[key] = (value, pointer)


        elif self.current_capacity < self.capacity:
            new_node = Node(key)

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

            self.index[self.current_pointer] = new_node

            self.hm[key] = (value, self.current_pointer)
            self.current_capacity += 1
            self.current_pointer += 1
        else:
            key_to_be_deleted = self.tail.value
            self.tail = self.tail.left
            self.tail.right = None

            _, pointer = self.hm[key_to_be_deleted]
            del self.hm[key_to_be_deleted]

            new_node = Node(key)

            node = self.head
            new_node.right = node
            node.left = new_node
            self.head = new_node

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
