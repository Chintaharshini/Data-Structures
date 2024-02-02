class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class DNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node
    def delete(self,data):
        if self.head is None:
            print("The LL is empty...")
        else:
            cur_node = self.head
            #beginning 
            if cur_node.data == data:
                self.head = cur_node.next 
                cur_node.next = None
                print("Element has deleted")
                return
            prev_node = self.head
            while cur_node is not None :
                if cur_node.data == data:
                    prev_node.next = cur_node.next
                    cur_node.next = None
                    print("Element has deleted")
                    return
                else:
                    prev_node = cur_node
                    cur_node = cur_node.next
    def printLL(self):
        if self.head is None:
            print("The LL is empty...")
        else:
            cur_node = self.head
            print("Forward LL traversal ... \n")
            while cur_node is not None:
                print(cur_node.data, end=" ")
                cur_node = cur_node.next
            print()
    def getLength(self,node=None):
        if node is None:
            return 0
        else:
            return 1+self.getLength(node.next)
    def reverseLL(self):
        cur_node = self.head
        if cur_node is None:
            print("List is empty")
            return
        else:
            prev = None
            next = None
            while cur_node:
                next = cur_node.next
                cur_node.next = prev
                prev = cur_node
                cur_node = next
            self.head = prev
            print("Reversed the LL")
            self.printLL()

                
class Dlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,data):
        if self.head is None:
            new_node = DNode(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node  = DNode(data)
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node       
            new_node.prev = cur_node
            self.tail = new_node
    def delete(self,data):
        if self.head is None:
            print("The DLL is empty...")
        else:
            cur_node = self.head
            #deletion at beginning
            if cur_node.data == data:
                self.head = cur_node.next
                self.head.prev = None
                print("Element has deleted")
                return
            #deletion at any position
            while cur_node.next is not None :
                if cur_node.data == data:                    
                    cur_node.prev.next = cur_node.next
                    cur_node.next.prev = cur_node.prev
                    cur_node.prev = None
                    cur_node.next = None
                    print("Element has deleted")
                    return
                else:
                    cur_node = cur_node.next
            #deletion at end
            if cur_node.data == data:
                cur_node.prev.next = None
                self.tail = cur_node.prev

    def printDLL(self):
        cur_node = self.head
        print("Forward traversal...\n")
        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()
        cur_node = self.tail
        print("Backward traversal...\n")
        while cur_node is not None:
            print(cur_node.data,end=" ")
            cur_node = cur_node.prev
        print()
'''
ll = Linkedlist()
ll.insert(2)
ll.insert(3)
ll.insert(5)
ll.insert(7)
ll.insert(8)
ll.insert(10)
#ll.printLL()
ll.delete(7)
ll.insert(12)
ll.printLL()

print(ll.getLength(ll.head))
ll.reverseLL()
'''

class StackLL:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        if self.top is None:
            return True
        else: 
            return False
    def push(self,data):
        if self.top is None:
            new_node = Node(data)
            self.top = new_node
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty.. underflow")
            return 
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.. underflow")
        else:
            return self.top.data
    def printstk(self):
        cur_node = self.top
        while(cur_node != None):
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()

class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100000
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def isFull(self):
        if self.top == self.max-1:
            return True
        return False
    def push(self,data):
        if self.isFull():
            print("Stack overflow")
            return -1
        else:
            self.array.append(data)
            self.top += 1
    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return -1
        else:
            element = self.array.pop()
            self.top -= 1
            return element
    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
            return -1
        else:
            peek = self.pop()
            self.push(peek)
            return peek

stk = Stack()
stk.push(2)
stk.push(5)
stk.push(8)
stk.push(7)
stk.push(9)
stk.pop()
stk.pop()
print(stk.peek())
