class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


class circular_linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
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
            new_node.prev=val.prev
            new_node.next=self.head
            val.prev.next=new_node
            self.head.prev=new_node

    def insert_at_beg(self,data):
        pass


    def traverse_for(self):
        val=self.head
        sta=self.head
        datas=""
        while val:
            datas += str(val.data)+"-->"
            val=val.next


            if sta == val:
                break
        print(datas)

    def traverse_rev(self):
        val=self.head.prev
        sta=self.head.prev
        datas=""
        while val:
            datas +=str(val.data)+"-->"
            val=val.prev

            if sta==val:
                break
        print(datas)


cc=circular_linkedlist()
cc.insert_at_end(1)
cc.insert_at_end(2)
cc.insert_at_end(3)
cc.insert_at_end(5)
cc.traverse_for()
cc.traverse_rev()
