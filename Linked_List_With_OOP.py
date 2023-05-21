class StackObj:
    
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n_object):
        if isinstance(n_object, StackObj) or n_object is None:
            self.__next = n_object


class Stack:
    def __init__(self):
        self.top = None
        self.last = None
    
    def push(self, n_obj):
        if self.last:
            self.last.next = n_obj
            
        self.last = n_obj
        if self.top is None:
            self.top = n_obj
    
    def pop(self):
        temp = self.top
        if temp is None:
            return
        while temp and temp.next != self.last:
            temp = temp.next
        if temp:
            temp.next = None
        last = self.last
        self.last = temp
        if self.last is None:
            self.top = None
        
        return last
    
    def get_data(self):
        lst = []
        temp = self.top
        while temp:
            lst.append(temp.data)
            temp = temp.next
        
        return lst
    

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
print(res)