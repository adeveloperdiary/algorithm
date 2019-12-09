"""
Runtime: 
1. union : O(n^2)
2. intersection : O(n^2)

Design:
1. Used a Linked List to store the array
2. Added find function in the LinkedList class
3. for union:
    1. Created a new empty Linked List (new_linked_list).
    2. Loop through the 1st LL, add uniqeue values to the empty Linked List
    3. Loop through the 2nd LL, add uniqeue values to the new_linked_list.
4. for intersection:
    1. Created a new empty Linked List (new_linked_list).
    2. Loop through 1st LL, verify whether the value is already in 2nd LL
    3. if True, then add the value to the new_linked_list

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def find(self, value):
        if self.head is None:
            return False
        else:
            node = self.head
            if node.value == value:
                return True
            while node.next:
                node = node.next
                if node.value == value:
                    return True

        return False


def union(llist_1, llist_2):
    new_linked_list = LinkedList()

    if llist_1 is not None and llist_1.head is not None:
        node = llist_1.head
        new_linked_list.append(node.value)
        while node.next:
            node = node.next
            if not new_linked_list.find(node.value):
                new_linked_list.append(node.value)

    if llist_2 is not None and llist_2.head is not None:
        node = llist_2.head
        if not new_linked_list.find(node.value):
            new_linked_list.append(node.value)
        while node.next:
            node = node.next
            if not new_linked_list.find(node.value):
                new_linked_list.append(node.value)

    return new_linked_list


def intersection(llist_1, llist_2):
    new_linked_list = LinkedList()

    if llist_1 is not None and llist_2 is not None:

        if llist_1.head is not None and llist_2.head is not None:

            node1 = llist_1.head
            node2 = llist_2.head

            if node1.value == node2.value:
                new_linked_list.append(node1.value)
            while node1.next:
                node1 = node1.next
                if llist_2.find(node1.value) and not new_linked_list.find(node1.value):
                    new_linked_list.append(node1.value)

    return new_linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))  # 3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11
print(intersection(linked_list_1, linked_list_2))  # 4, 6, 21

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # 3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21
print(intersection(linked_list_3, linked_list_4))  # Empty List
