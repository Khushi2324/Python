class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def push(self,data): # Inserting node at end of linked list O(n)
        Newnode=Node(data)
        if self.head is None:
            self.head=Newnode
            return

        last=self.head

        while(last.next):
            last=last.next
        last.next=Newnode

    def print(self):
        t1=self.head
        while(t1):
            print(t1.data)
            t1=t1.next

    def n_element_from_lst(self,index):
        current=self.head
        count=0
        while(current):
            if (count==index):
                return current.data
            count=count+1
            current=current.next


llist=Linked_list()
llist.push(2)
llist.push(3)
llist.push(5)
llist.push(6)
llist.push(7)
llist.print()

print(llist.n_element_from_lst(2))





