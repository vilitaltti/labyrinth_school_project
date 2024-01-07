from linkedlist import LinkedList

class Stack():

    def __init__(self):
        self.list = LinkedList()
        

    def top(self):
        if self.list.head != None:
            return self.list.head.get_data()
        else:
            return None

    def is_empty(self):
        if self.list.head == None and self.list.tail == None:
            return True
        else:
            return False

    def pop(self):
        tmp =  self.list.remove_first()
        if tmp == None:
            return None
        return tmp.get_data()

    def push(self,data):
        self.list.add_first(data)
