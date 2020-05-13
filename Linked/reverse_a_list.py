class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def __isEmpty__(self):
        return (self.head==None)

    def push(self,data):
        newnode=Node(data)
        if self.__isEmpty__():
            self.head=newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def reverse_a_list(self):
        curr=self.head
        prev=None
        next=None

        while(curr):
            next,curr.next=curr.next,prev
            prev,curr=curr,next

        self.head=prev


    def print_list(self):
        if self.__isEmpty__():
            print("List is Empty")

        curr=self.head
        while(curr):
            print(curr.data,end=" ")
            curr=curr.next



llist=Linked_list()
llist.push(3)
llist.push(2)
llist.push(1)
llist.print_list()
llist.reverse_a_list()
print("\n")
llist.print_list()
