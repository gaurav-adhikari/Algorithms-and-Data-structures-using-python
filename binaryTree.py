# Playing with Trees


def simpleBinaryTree():
    simpleBinaryTree = ['15',
                        ['6',
                         ['5', '7']],
                        ['10',
                         ['9']]]

    print(simpleBinaryTree)
    print("Root: ", simpleBinaryTree[0])
    print("left subtree ", simpleBinaryTree[1])
    print("Right subtree", simpleBinaryTree[2])


# Builds a generic binary tree
def binaryTreeBuilder(root):
    return [root, [], []]


def leftNodeInsertion(myRoot, leftsubTree):
    childPlaceHolder = myRoot.pop(1)
    if(len(childPlaceHolder) > 1):
        myRoot.insert(1, [leftsubTree, childPlaceHolder, []])
    else:
        myRoot.insert(1, [leftsubTree, [], []])

    return myRoot


def rightNodeInsertion(myRoot, rightSubTree):
    childPlaceHolder = myRoot.pop(2)
    if len(childPlaceHolder) > 1:
        myRoot.insert(2, [rightSubTree,  [], childPlaceHolder])
    else:
        myRoot.insert(2, [rightSubTree, [], []])
    return myRoot


def rootgetter(myRoot):
    return myRoot[0]


def leftChildGetter(myRoot):
    return myRoot[1]


def rightChildGetter(myRoot):
    return myRoot[2]


# Approach2 of creating binary trees
class BinaryApproach2:
    def __init__(self, myRoot):
        self.key = myRoot
        self.rightWing = None
        self.leftWing = None

    # adds the left wing
    def leftNodeInsertion(self, leftSubTree):
        if self.leftWing == None:
            self.leftWing = leftSubTree
        else:
            newNode = BinaryApproach2(leftSubTree)
            newNode.leftWing = self.leftWing
            self.leftWing = newNode

    # adds the right wing 
    def rightNodeInsertion(self, rightSubTree):
        if self.rightWing == None:
            self.rightWing = rightSubTree
        else:
            newNode = BinaryApproach2(rightSubTree)
            newNode.rightWing = self.rightWing
            self.rightWing = newNode

    # Returns left wing of tree
    def leftChildGetter(self):
        return self.leftWing

    # Returns right wing of tree
    def rightChildGetter(self):
        return self.rightWing

    # Returns root of the tree
    def rootgetter(self):
        return self.key


def main():

    # simpleBinaryTree()  # Create a simple binary tree

    # Gernerically creating binary tree
    tree = binaryTreeBuilder(10)

    leftNodeInsertion(tree, 9)
    leftNodeInsertion(tree, 8)
    rightNodeInsertion(tree, 11)
    rightNodeInsertion(tree, 3)

    # Assertioin tests
    assert tree == [10, [8, [9, [], []], []], [3, [], [11, [], []]]]
    assert rootgetter(tree) == 10
    assert leftChildGetter(tree) == [8, [9, [], []], []]
    assert rightChildGetter(tree) == [3, [], [11, [], []]]

    # Approach2 test case
    myTree = BinaryApproach2('a')
    assert myTree.rootgetter() == "a"

    myTree.leftNodeInsertion('b')
    myTree.leftChildGetter() == "b"

    myTree.rightNodeInsertion('d')
    assert myTree.rightChildGetter() == "d"

    myTree.leftNodeInsertion("c")
    assert myTree.leftChildGetter().rootgetter() == "c"

# Graphical Tree representation  

    """
        a
      /   \
    b       d
   /
 c
    """

    pass


if __name__ == '__main__':
    main()

'''
Conclusion
            -> Trees are beautiful and alot powerful
            -> OOPS is very beautiful 
'''
