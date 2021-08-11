class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class linked_list:
    def __init__(self,head=None):
        self.head=head


    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head==None:
            node=Node(data,None)
            self.head=node
        else:
            val=self.head
            while val:
                if val.next == None:
                    node=Node(data,None)
                    val.next=node
                    break
                val=val.next
    def insert_at_middle(self,data,index):
        length=self.len()
        val=self.head
        count=1
        while val:
            count +=1
            if count== index:
                node=Node(data,val.next)
                val.next=node
            # else:
            #     print("Your index is greater than the length of the list")
            #     print("Enter a value between {}".format(length))

            val=val.next
    def  delete(self,data):
        val=self.head
        count=0
        while val:
            count += 1
            if val.data== data:
                count -=1
                break
            val=val.next
        value=self.head
        i=1
        while i<count:
            value=value.next
            i=i+1
        value.next=value.next.next





    def len(self):
        val=self.head
        count=0
        while val:
            count=count+1
            val=val.next
        return count



    def print(self):
        val=self.head
        st=""
        while val:
            st += str(val.data)+"-->"
            val=val.next
        print(st)


a=linked_list()
a.insert_at_end(10)
a.print()
a.insert_at_end(11)
a.insert_at_end(12)
a.insert_at_end(13)
a.print()
a.insert_at_middle(89,3)
a.print()
a.insert_at_beginning(6)
a.print()
a.delete(89)
a.print()
