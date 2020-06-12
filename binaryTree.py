# Playing with Trees

def simpleTree():
    myTree = ['a',
        ['b',
            ['d','e']],
        ['c' ,
            ['f']] ]
    
    print(myTree)
    print("Root: ",myTree[0])
    print("left subtree ",myTree[1])
    print("Right subtree",myTree[2])


def main():
    simpleTree()
    pass

if __name__=='__main__':
    main()

'''
Conclusion
            -> Trees are beautiful and alot powerful
'''