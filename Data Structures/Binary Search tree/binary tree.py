class binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add(self,data):
        if data > self.data:
            if self.right:
                self.right.add(data)
            else:
                self.right=binary_tree(data)

        else:
            if self.left:
                self.left.add(data)
            else:
                self.left=binary_tree(data)

    def inorder(self,li=[]):

        if self.left:
            self.left.inorder()

        li.append(self.data)

        if self.right:
            self.right.inorder()
        return  li
    def preorder(self,li=[]):
        li.append(self.data)
        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

        return li


a=binary_tree(100)
data=[10,2,33,5,32,324,22,212,454,234]
def add_values(data):
    for i in data:
        a.add(i)

add_values(data)
print(a.inorder())
print(a.preorder())
