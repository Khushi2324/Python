class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

def merge(L1,L2):
    L3=Node(None,None)  #Create Empty List
    prev=L3

    while (L1!=None and L2!=None):
        if L1.data<L2.data:
            prev.next=L1
            L1=L1.next
        else:
            prev.next=L2
            L2=L2.next
        prev=prev.next

    if L1 is None:
        prev.next=L2
    else:
        prev.next=L1
    return L3




n3=Node(10,None)
n2=Node(3,n3)
n1=Node(2,n2)
L1=n1

n6=Node(8,None)
n5=Node(7,n6)
n4=Node(4,n5)
L2=n4

merged=merge(L1,L2)

while merged!=None:
    print(merged.data)
    merged=merged.next
print("None")








