class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def print_list(self):
        import pdb ;pdb.set_trace()
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next


llist=Linked_list()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next = second
second.next=third

llist.print_list()







