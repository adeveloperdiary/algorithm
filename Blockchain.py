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
        self.head = None

    def add(self, data):
        print("Execute Add")
        now_GMT = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")

        if self.head is not None:
            temp = self.head
            node = Block(now_GMT, data, self.head.hash)
            node.prev = temp
            self.head = node
        else:
            self.head = Block(now_GMT, data, '0')

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
        print("Execute Delete")
        if self.head is not None:
            if self.head.hash == hash:
                if self.head.prev is not None:
                    self.head = self.head.prev
                else:
                    self.head = None
            else:
                node = self.head
                while node.prev is not None:
                    next = node
                    node = node.prev
                    if node.hash == hash:
                        if node.prev is None:
                            next.previous_hash = '0'
                            next.prev = None
                            node = None
                            break
                        else:
                            next.previous_hash = node.prev.hash
                            next.prev = node.prev
                            node = None
                            break

    def display(self):
        str = ''

        if self.head is not None:
            node = self.head
            if node.prev is None:
                str += '( ' + node.data + ' )'
            else:
                str += '( ' + node.data + ' )'
                while node.prev is not None:
                    node = node.prev
                    str += '->( ' + node.data + ' )'

        print('Current BlockChain: ' + str)


if __name__ == "__main__":
    bc = BlockChain()
    hash1 = bc.add("1")
    hash2 = bc.add("2")
    hash3 = bc.add("3")
    hash4 = bc.add("4")
    bc.display()  # print ( 4 )->( 3 )->( 2 )->( 1 )

    find = bc.get(hash1)

    print(find.data)  # Print 1

    bc.delete(hash3)
    bc.display()  # print ( 4 )->( 2 )->( 1 )
    bc.delete(hash4)
    bc.display()  # print ( 2 )->( 1 )
    bc.delete(hash1)
    bc.display()  # print ( 2 )
    bc.delete(hash2)
    bc.display()  # print ''
    bc.delete(hash1)
    bc.display()  # print ''
    find = bc.get(hash1)
    print(find)  # print None
