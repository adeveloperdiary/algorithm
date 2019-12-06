import sys
from collections import defaultdict, OrderedDict
import heapq


class Node:
    def __init__(self, value):
        self.value = value
        self.root = None
        self.left = None
        self.right = None
        self.data = None
        self.data_dict = dict()

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str("{} : {}".format(self.value, self.data, self.data_dict))


def huffman_encoding(data):
    frequency = defaultdict(int)

    for c in data:
        frequency[c] += 1

    sorted_freq = OrderedDict(sorted(frequency.items(), key=lambda x: x[1], reverse=False))

    heap = []

    for i, key in enumerate(sorted_freq):
        val = sorted_freq[key]
        node = Node(val)
        node.data = key

        heapq.heappush(heap, node)

    while len(heap) > 1:
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap)

        val = node_1.value + node_2.value
        root = Node(val)
        node_1.root = root
        node_2.root = root
        root.left = node_1
        root.right = node_2

        new_dict = dict()

        if len(node_1.data_dict) > 0:
            for key in node_1.data_dict:
                new_dict[key] = '0' + node_1.data_dict[key]
        else:
            new_dict[node_1.data] = '0'

        if len(node_2.data_dict) > 0:
            for key in node_2.data_dict:
                new_dict[key] = '1' + node_2.data_dict[key]
        else:
            new_dict[node_2.data] = '1'

        root.data_dict = new_dict
        heapq.heappush(heap, root)

    root = heapq.heappop(heap)

    encoded = ''
    for c in data:
        encoded += root.data_dict[c]

    return encoded, root


def huffman_decoding(data, tree: Node):
    decoded = ''
    node = tree
    for i in range(len(data)):
        if data[i] == '0':
            node = node.left
        else:
            node = node.right

        if node.data is not None:
            decoded += node.data
            node = tree
    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
