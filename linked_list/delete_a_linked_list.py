class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def delete(self):
        current=self.head
        while(current):
            prev=current.next

            del current.data
            current=prev

    def print_list(self):
        temp=self.head
        if temp is None:
            print("Linked List is empty")
        while(temp):
            print(temp.data)
            temp=temp.next


llist=Linked_list()
llist.push(8)
llist.push(6)
llist.push(8)
llist.print_list()
llist.delete()

h=Linked_list()
h.print_list()

