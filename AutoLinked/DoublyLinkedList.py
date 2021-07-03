
from typing import List, Tuple


class Node:

    def __init__(self, value : int, next = None , prev = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    verbose = 0

    def __init__(self, verbose = 0) -> None:
        self.root = None
        self.verbose = verbose
    
    def __insert_to_list(self, key : int):

        if self.root == None:
            self.root = Node(key)
        
        temp_node = Node(key)
        temp_node.next = self.root
        temp_node.prev = None
        self.root = temp_node

        self.root.prev = temp_node        

    def __print_doubly(self):

        temp_node = self.root
        while(temp_node.next):
            if temp_node.next.next:
                print(temp_node.value,end=" <-> ")
            else:
                print(temp_node.value,end="\n")
            temp_node = temp_node.next

    def doubly(self,array : List[int], sorted = False , sorted_descending = False):

        if sorted:
            if sorted_descending:
                array.sort(reverse=False)
            else:
                array.sort(reverse=True)
        else:
            array = reversed(array)
        for element in array: self.__insert_to_list(element)
        if self.verbose:
            self.__print_doubly()
        
        return self.root
        





# cl = DoublyLinkedList(verbose=1)
# # cl2 = LinkedList()
# cl.doubly([1,2,22,7,4,5],sorted=False,sorted_descending=False)
# cl2.singly([1,2,3,4,5])