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

    def inorder(self):
        li=[]

        if self.left:
            li+=self.left.inorder()

        li.append(self.data)

        if self.right:
            li+=self.right.inorder()
        return  li
    def preorder(self):
        li=[]
        li.append(self.data)
        if self.left:
            li+=self.left.preorder()

        if self.right:
            li+=self.right.preorder()

        return li

    def postorder(self):
        li = []
        if self.left:
            li+=self.left.postorder()
        if self.right:
            li+=self.right.postorder()

        li.append(self.data)

        return li

    def max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.min()


    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self



a=binary_tree(100)
data=[10,2,33,5,32,324,22,212,454,234]
def add_values(data):
    for i in data:
        a.add(i)

add_values(data)
print(a.inorder())
print(a.preorder())
print(a.postorder())
print(a.max())
print(a.min())
print(a.left.right.left.min())
print(a.inorder())
a.delete(10)


print(a.inorder())
