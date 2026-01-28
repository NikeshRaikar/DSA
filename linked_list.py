# Author : Nikesh Jagadeesh Raikar
# Date: Jan 28, 2026

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:

    # constructor
    def __init__(self, value):
        new_node = Node(value)
        self.tail = new_node    # self.tail.next is none
        self.head = new_node
        self.length = 1



    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = None

        self.length+=1

    def print_list(self):
        pass

    def pop(self): # this is 0(n) as we need to iterate from head
         if self.length == 0:  # we check if length of LL is 0, if True then we return None
             return None
         # If self.length is not 0, then we create a temp and pre variable to iterate and reach the last element in LL
         temp = self.head
         pre = self.head
         while temp.next:
            pre = temp
            temp = temp.next
         self.tail = pre
         self.tail.next = None
         self.length -= 1
         if self.length == 0:
             self.head = None
             self.tail = None
