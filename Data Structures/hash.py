class Hashtable:
    def __init__(self):
        self.max=10
        self.arr= [[] for i in range(self.max)]

    def gethash(self,key):
        hash=0
        for i in key:
            hash +=ord(i)
        return  hash % self.max
    def add(self,key,value):
        hash=self.gethash(key)
        val=0
        for idx,ele in enumerate(self.arr[hash]):
            if ele[0]==key:
                self.arr[hash][idx]=(key,value)
                val=1

        if val==0:
            self.arr[hash].append((key,value))

    def get(self,key):
        hash=self.gethash(key)
        for idx,ele in enumerate(self.arr[hash]):
            if ele[0]==key:
                print(self.arr[hash][idx][1])

    def print(self):
        for i in self.arr:
            print(i)







t=Hashtable()
t.add("may 1",10)
t.add("may 2",20)
t.add("may 3",30)
t.add("may 5",40)
t.add("may 4",50)
t.add("may 6",60)
t.add("may 7",28)
t.add("may 8",78)
t.add("may 9",72)
t.add("may 10",98)
t.add("may 11",70)
t.add("may 12",128)
t.get("may 6")


t.print()