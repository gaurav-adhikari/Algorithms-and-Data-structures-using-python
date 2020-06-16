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

    pass


if __name__ == '__main__':
    main()

'''
Conclusion
            -> Trees are beautiful and alot powerful

'''
