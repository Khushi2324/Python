class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def swap_adjacent(self):
        temp=self.head
        while(temp is not None and temp.next is not None):
            temp.data,temp.next.data =temp.next.data,temp.data
            temp=temp.next.next


    def push(self,data):
        new_node=Node(data)
        if (self.head==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node


    def print_list(self):
        if self.head==None:
            print("Empty List")
        else:
            temp=self.head
            while(temp):
                print(temp.data, end=" ")
                temp=temp.next


li=Linked_List()
li.push(6)
li.push(5)
li.push(4)
li.push(3)
li.push(2)
li.push(1)
li.print_list()
li.swap_adjacent()

print()
li.print_list()

