class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[]
        self.parent=None

    def add_child(self,data):
        data.parent=self
        self.child.append(data)


    def print(self):
        print(self.data) #o(n)^3
        for i in self.child:
            print(" |",i.data)
            for j in i.child:
                print("   |",j.data)
                for k in j.child:
                    print("     |",k.data)

    def print_l(self,level=0):
        print(" "*level+"|",self.data) #o(n)^3
        level=level+1
        for i in self.child:
            i.print_l(level)
a=Tree("PC")
laptop=Tree("Laptop")
apple=Tree("Apple")
apple.add_child(Tree("Macbook 2020"))
apple.add_child(Tree("Macbook air 2020"))
laptop.add_child(apple)
laptop.add_child(Tree("HP"))
laptop.add_child(Tree("Lenovo"))
a.add_child(laptop)

computers=Tree("Computers")
computers.add_child(Tree("Apple"))
computers.add_child(Tree("HP"))
computers.add_child(Tree("Dell"))
a.add_child(computers)

b=Tree("Mobile")
ios=Tree("Ios")
ios.add_child(Tree("Apple Iphone 12 Pro Max"))
ios.add_child(Tree("Apple Iphone 12 "))
ios.add_child(Tree("Apple Iphone 11 Pro Max "))
ios.add_child(Tree("Apple Iphone 11 "))
ios.add_child(Tree("Apple Iphone XR "))
b.add_child(ios)

a.print_l()
b.print_l()