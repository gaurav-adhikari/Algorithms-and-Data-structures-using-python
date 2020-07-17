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

    def size(self):
        return self.length

    def putNode(self, key, val):

        # Condtiion to check the root and if not available create one using the Node class
        if self.root:
            self.putHelper(key,vak,self.root)
        else:
            self.root=Node(key,val)
        
        self.size+=1
        pass    

    def putHelper(self, key,val,currentNode):

        # Condition for the left child
        if key<currentNode.key:
            # check for the availability of left child

            # if left child is present, recursively call this function
            if currentNode.hasLeftChild():
                self.putHelper(key,val,currentNode.leftChild)
            
            #if not,create a new left child Node  
            else:
                currentNode.leftChild=Node(key,val,parentNode=currentNode)
        
        # For the right child
        else:
            if currentNode.hasRightChild():
                self.putHelper(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=Node(key,val,parentNode=currentNode)
        pass
    

    def getNode(self,key):

        if self.root:
            tempNode=getHelper(self,key,self.root)
            
            # return the dat- 
            if tempNode:
                return tempNode.data
            else:
                return None
        else:
            return None


    def getHelper(self,key,currentNode):

        
        if currentNode==None:
            return None

        # check the key for each resulting Node
        elif currentNode.key==key:
            return currentNode
        elif currentNode.key<key:
            return self.getHelper(key,currentNode.leftChild)
        else:
            return self.getHelper(key,currentNode.rightChild)

    
    # Overloading the "in" operator
    def __contains__(self,key):
        if self.getHelper(key,self.root):
            return True
        else:
            return False

    def nodeDeletion(self, key):

        # check the number of nodes in the tree

        if self.size >1 :

            deletionNode=getHelper(key,self.root)
            # TODO
            #  -> delete only after the selected node is identified by the key
            


'''
 Constructing a helper function

      Node

left        right


-> every child carries a value or a payload
-> information about left child and right child

'''


class Node:

    def __init__(self, key, data, leftChild=None, rightChild=None, parentNode):
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
