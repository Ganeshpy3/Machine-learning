class node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next

class Doubly_linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        new_node = node(data)
        if self.head is None:

            self.head=new_node

        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node

    def insert_at_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.insert_at_begin(data)
        else:
            val=self.head
            while val.next:
                val=val.next

            new_node.prev=val
            val.next=new_node
    def insert_at_middle(self,data,index):
        if index==0:
            self.insert_at_begin(data)
        else:
            val=self.head
            new_node=node(data)
            ind=0
            while val and ind<index:
                ind =ind+1
                val=val.next

            new_node.next=val
            new_node.prev=val.prev
            val.prev.next=new_node
            val.prev=new_node

    def lenght(self):
        val=self.head
        leng=0
        while val:
            leng+=1
            val=val.next

        return leng
    def delete(self,index):
        leng=self.lenght()
        print(leng)
        if leng < index:
            print("Index Out of range")

        elif index==1:
            self.head=self.head.next
            self.head.prev=None
        elif leng==index:
            val=self.head
            index1=1
            while val and index1<index:
                val=val.next
                index1+=1

            val.prev.next=None

        else:
            val=self.head
            inde=0
            while val and inde<index-1:
                inde= inde+1
                val=val.next
            t=val.next
            val.next.prev=val.prev
            val.prev.next=t




    def traverse(self):
        val=self.head
        st=""
        while val:
            st +=str(val.data)+"-->"
            val=val.next
        print(st)
    def reverse_trav(self):
        val=self.head
        while val.next:
            val=val.next

        val1=val
        st=""
        while val1:
            st +=str(val1.data)+"-->"
            val1=val1.prev
        print(st)

dll=Doubly_linkedlist()
dll.insert_at_begin(5)
dll.insert_at_begin(6)
dll.insert_at_end(8)
dll.insert_at_end(7)
dll.insert_at_end(9)

dll.insert_at_begin(20)
dll.traverse()
dll.delete(2)
dll.insert_at_middle(100,2)
dll.traverse()
dll.reverse_trav()
# dll.traverse()
# dll.reverse_trav()





