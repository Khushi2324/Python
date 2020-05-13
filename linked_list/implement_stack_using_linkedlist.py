class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack():
    def __init__(self):
        self.head=None

    def push(self,data):
        newnode=Node(data)

        if self.isEmpty():
            self.head=newnode
            return
        newnode.next=self.head
        self.head=newnode
        
    def isEmpty(self):
        if self.head is None:
            return True
        else :
            return False

    def pop(self):
        if not self.isEmpty():
            popped=self.head.data
            self.head=self.head.next
            return popped

    def print_stack(self):
        temp=self.head
        if self.isEmpty():
            print("Empty Stack")
        while(temp):
            print(temp.data)
            temp=temp.next
            


stack=Stack()
stack.push(1)
stack.push(2)
stack.print_stack()
stack.pop()
stack.print_stack()


