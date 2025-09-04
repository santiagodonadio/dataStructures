class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def display(self):
        current = self.head
        elements = []
        
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))
        
    def delete(self, data):
        
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
        
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.display()

my_list.delete(20)

