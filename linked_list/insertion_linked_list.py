class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insert_after_node(self,prev_node,newdata):
        newnode=Node(newdata)
        if prev_node is None:
            print(" Node must be in Linked list")
        newnode.next=prev_node.next
        prev_node.next=newnode

    def insert_at_end(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode

    def print_list(self):
        l=self.head
        while(l):
            print(l.data)
            l=l.next


llist=Linked_list()
llist.insert_at_beg(8)
llist.insert_at_beg(9)
llist.insert_at_end(10)
llist.insert_after_node(llist.head.next,5)
llist.print_list()