import hashlib
import datetime


def calc_hash(self):
    sha = hashlib.sha256()

    hash_str = "We are going to encode this string of data!".encode('utf-8')

    sha.update(hash_str)

    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


class BlockChain:
    def __init__(self):
        self.tail = None
        self.total_size = 0
        self.head = None

    def add(self, data):
        now_GMT = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

        if self.head is not None:
            self.head = Block(now_GMT, data, self.current.hash)

        else:
            self.head = Block(now_GMT, data, 0)
            self.tail = self.head

        return self.head.hash

    def get(self, hash):
        pass

    def delete(self, hash):
        pass
