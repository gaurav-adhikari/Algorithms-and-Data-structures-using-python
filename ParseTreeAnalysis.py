# Implentation of parse tree in python

# Importing necessary datastructures for the parseTree
import operator
from binaryTree import BinaryApproach2
from ExploringPythonStacks import MyStack

# Function to build a pass tree


def passTreeBuilder(myExpression):
    myExpressionList = myExpression.split()
    myStack = MyStack()
    myBinaryTree = BinaryApproach2('')

    myCurrentTree = myBinaryTree

    for i in myExpression:
        if i == "(":
            myBinaryTree.leftNodeInsertion('')
            myStack.push(myCurrentTree)
            myCurrentTree = myBinaryTree.leftChildGetter()

        elif i in ['+', '-', '*', '/']:
            myBinaryTree.setRootVal(i)
            myBinaryTree.rightNodeInsertion('')
            myStack.push(myCurrentTree)
            myCurrentTree = myBinaryTree.rightChildGetter()

        elif i == ')':
            myStack.pop()

    return myBinaryTree


# def evaluateParseTree(myParseTree):
    
#     # Mapping a dictionary to their respective intrinsic python arithmetic library
#     opers = {'+': operator.add, '-': operator.sub,
#              '*': operator.mul, '/': operator.truediv}
    
#     leftchild = myParseTree.leftChildGetter()
#     rightchild = myParseTree.rightChildGetter()

#     if leftchild and rightchild:
#         operfn = opers[myParseTree.rootgetter()]
#         return operfn(evaluateParseTree(leftchild),evaluateParseTree(rightchild))

#     else:
#         return myParseTree.rootgetter()

def main():

    passTreeBuilder("( (1 + 2) * 3")
    

if __name__ == "__main__":
    main()


"""
//TODO

-> Keep track of root node as well as parent node
-> use stack to keep track of the parent node
-> split the operators and push to left and right node accordingly analysing the paranthesis
-> Evalutate the parse tree

"""
