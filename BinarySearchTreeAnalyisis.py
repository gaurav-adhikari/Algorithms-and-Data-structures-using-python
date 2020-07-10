# Binary Tree Analysis in python

'''

        a

b<a          c>a

-> Build a helper class to keep track of nodes

'''


class BST:

    def __init__(self):
        self.root = None
        self.length = 0

    def length(self):
        return self.length


'''
 Constructing a helper function

      Node

left        right


-> every child carries a value or a payload
-> information about left child and right child

'''


class Node:
    
    def __init__(self, key, data, leftChild, rightChild, parentNode):
        self.key = key
        self.data = data
        self.leftchild = leftChild
        self.rightChild = rightChild
        self.parentNode = parentNode

    # Miscellaneous functions
    
    # function to check a given Node has any left child 
    def hasLeftChild(self):
        return self.leftchild

    # function to check a given Node has any right child 
    def hasRightChild(self):
        return self.rightChild

    # function to check a given has any child 
    def hasAnyChild(self):
        return self.leftchild or self.rightChild

    #  function to check if both 
    def hasBothChildren(self):
        return self.leftchild and self.rightChild

    # function to check if the functin is leaf 
    def isLeaf(self):
        return not (self.leftchild or self.rightChild)

    # function to check if the given node is root
    def isRoot(self):
        return not self.parentNode

    # A function to replace node data
    def replaceNode(self, key, newData, newLeftChild, newRightChild):
        self.key = key
        self.data = newData
        self.leftchild = newLeftChild
        self.rightChild = newRightChild

        # set the root nodes of the respective childs to current object
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.hasRightChild():
            self.rightChild = self
        



def main():
    pass


if __name__ == "__main__":
    main()
