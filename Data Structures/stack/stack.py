
class stack:
    def __init__(self):
        self.stack=[]

    def add(self,data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            self.stack.pop()

    def display(self):
        print(self.stack[-1::-1])


st=stack()
st.add(1)
st.add(2)
st.add(3)
st.display()
st.pop()
st.display()
st.add(6)
st.display()