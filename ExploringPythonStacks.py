# A basic implementation of Stack in python using abstract datatype


# Creating basic Stack Operations from python lists
class MyStack:

    def __init__(self):
        self.items=[]

    # complexity O(n)
    def pop(self):
        return self.items.pop(0)

    # Complexity O(n)
    def push(self,item):
        return self.items.insert(0,item)

    # Complexity O(n)
    def size(self):
        return len(self.items)

    # Complexity O(1)
    def peek(self):
        return self.items[0]

    # 
    def isEmpty(self):
        return self.items == []
    

def main():
    # Creating an instance of MyStack Class
    stack = MyStack()

    # Testing memeber functions
    print(stack.push('gaurav'))
    print(stack.peek())
    print(stack.size())
    print(stack.pop())
    print(stack.size())


if __name__=="__main__":
    main()
    



'''
 Conclusion
            -> Explored different operations and time complexities associated abstract data type
'''