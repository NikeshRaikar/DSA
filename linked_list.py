# Author : Nikesh Jagadeesh Raikar
# Date: Jan 28, 2026
# from cgi import print_arguments


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
            self.tail = new_node


        self.length+=1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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

    # def pop_first(self):
    #     if self.length ==0:
    #         return False
    #     temp = self.head
    #     self.head = temp.next
    #     temp.next = None
    #     if self.length == 0:
    #         self.head = None
    #         self.tail = None


    def insert(self, index, value):
        new_node= Node(value)
        # Edge Scenarios
            # Index is out of range
            # Length of list is 0
        if index > self.length or index < 0:
            return False
        if index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        if index ==0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True
        else:
            temp = self.head
            pre = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = new_node
            new_node.next = temp
            self.length +=1
            return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
        return True


    def pop_first(self):
        if self.length == 0:
            return False
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.length -= 1
        return temp

    def get(self, index):
        if index > self.length or index < 0:
            return False
        temp = self.head
        for _ in range(index-1):
            temp= temp.next
        return temp








ll = Linked_list(5)
ll.append(6)
ll.append(44444444444444444)
ll.append(5555555555555)
ll.append(6)
ll.append(6)
ll.append(6)
ll.print_list()
print("----------------------------------------------------")
print(ll.length)
print("----------------------------------------------------")

ll.insert(7, 10)
ll.insert(3, 10)
ll.insert(5, 10)
ll.insert(6, 10)
ll.prepend(777)
ll.prepend(89)
# Just a test

print("Printing the poped item")

print("getting third item")
print(ll.get().value)




print("-------------------------7777---------------------------")
print(ll.length)
print("-------------------------7777---------------------------")
ll.print_list()