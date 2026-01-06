class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head=None):
        if head == None:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            head_node = Node(head)
            self.head = head_node
            self.tail = head_node
            self.size = 1

    def push_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def push_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        if not self.head: raise IndexError("The linked list is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def pop_back(self):
        if not self.head: raise IndexError("The linked list is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def __str__(self):
        print_arr = []
        current = self.head
        while current != None:
            print_arr.append(str(current.value))
            current = current.next
        return " ".join(print_arr)