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

    def print_list(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

    def detect_loop(self):
        temp1=self.head
        temp2=self.head
        while(temp1 and temp2 and temp2.next):
            temp1=temp1.next
            temp2=temp2.next.next
            if temp1==temp2:
                print("\nFound Loop")
                return temp1.data

llist=Linked_list()
llist.push(20)
llist.push(4)
llist.push(5)
llist.push(10)
llist.print_list()
llist.head.next.next.next=llist.head
p=llist.detect_loop()
print(p)


