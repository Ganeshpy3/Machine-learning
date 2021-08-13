class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


class circular_linkedlist:
    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.head.prev=self.head
            self.head.next=self.head

        else:
            sta=self.head
            val=self.head
            # [1,2]
            while val.next:

                val=val.next
                if val == sta:
                    break
            new_node.prev=val
            new_node.next=sta
            val.next=new_node

    def printx(self):
        val=self.head
        sta=self.head
        while val:
            print(val.data)
            val=val.next
            if val == sta:
                break



cc=circular_linkedlist()
cc.add(1)
cc.add(2)
# cc.add(3)
cc.printx()