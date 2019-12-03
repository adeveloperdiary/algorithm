import hashlib
import datetime


class Block:

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (str(datetime.datetime.now()) + "We are going to encode this string of data!").encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None


class BlockChain:
    def __init__(self):
        self.tail = None
        self.total_size = 0
        self.head = None

    def add(self, data):
        now_GMT = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

        if self.head is not None:
            temp = self.head
            node = Block(now_GMT, data, self.head.hash)
            node.prev = temp
            self.head = node

        else:
            self.head = Block(now_GMT, data, '0')
            self.tail = self.head

        return self.head.hash

    def get(self, hash):

        if self.head is not None:
            if self.head.hash == hash:
                return self.head
            else:
                node = self.head
                if node.hash == hash:
                    return node
                while node.prev is not None:
                    node = node.prev
                    if node.hash == hash:
                        return node
                return None
        else:
            return None

    def delete(self, hash):
        pass


if __name__ == "__main__":
    bc = BlockChain()
    hash1 = bc.add("1")
    print(hash1)
    hash2 = bc.add("2")
    print(hash2)
    hash3 = bc.add("3")
    print(hash3)

    find = bc.get(hash1)

    print(find.data)
