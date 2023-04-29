import sys


#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = "foo bar baz foo1 bar1 baz1".split()

class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None
        
    def link(self, obj):
        self.next_obj = obj

head_object = ListObject(lst_in[0])
temp_object = head_object
for i in range(1, len(lst_in)):

    new_object = ListObject(lst_in[i])
    temp_object.link(new_object)
    #print(temp_object.__dict__)
    temp_object = new_object
    
    
#print(temp_object.__dict__)