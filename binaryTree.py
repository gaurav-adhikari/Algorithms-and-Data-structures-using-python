# Playing with Trees

def simpleTree():
    simpleBinaryTree = ['15',
        ['6',
            ['5','7']],
        ['10' ,
            ['9']] ]
    
    print(simpleBinaryTree)
    print("Root: ",simpleBinaryTree[0])
    print("left subtree ",simpleBinaryTree[1])
    print("Right subtree",simpleBinaryTree[2])


def main():
    simpleTree()
    pass

if __name__=='__main__':
    main()

'''
Conclusion
            -> Trees are beautiful and alot powerful
'''