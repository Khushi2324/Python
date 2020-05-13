class Node:
    def __init__(self,data=None):
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
        if self.head==None:
            print("Empty List")
        else:
            temp=self.head
            while(temp):
                print(temp.data, end=" ")
                temp=temp.next

    def reverse_a_linked_lista(self,curr,prev):
        if curr.next is None:
            self.head=curr

            curr.next=prev
            return

        p=curr.next
        curr.next=prev
        self.reverse_a_linked_lista(p,curr)




    def reverse_a_linked_list(self):
        if self.head is None:
            return
        self.reverse_a_linked_lista(self.head,None)



llist=Linked_list()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)

print("Given List")
llist.print_list()

llist.reverse_a_linked_list()
print("\nReverse List")
llist.print_list()


