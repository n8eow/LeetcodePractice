class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.Table = [None]*capacity


    def add(self, key):
        index = key%self.capacity
        node = self.Table[index]
        while node:
            if node.key == key:
                return
            node = node.next
        New_node = ListNode(key)
        New_node.next = self.Table[index]
        self.Table[index] = New_node



    def remove(self, key):
        index = key%self.capacity
        node = self.Table[index]
        if node and node.key == key:
            self.Table[index] = node.next
            return
        pre = None
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre = node
            node = node.next

    def contains(self, key):
        index = key%self.capacity
        node = self.Table[index]

        while node:
            if node.key == key:
                return True
            node = node.next
        return False


