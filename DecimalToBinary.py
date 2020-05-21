# A program to convert a decimal number into binary 

from ExploringPythonStacks import MyStack

def divisionByTwo(decimalNum):
    
    # Using the stack from my previous program
    myStack=MyStack()

    while decimalNum>0:
        remainder = decimalNum%2
        myStack.push(remainder)
        decimalNum=decimalNum//2

    return myStack

def returnBinary(mystack):
    
    finalBinString=''
    
    # convert and Concatenate all the binary strings 
    while not mystack.isEmpty():
        finalBinString+=str(mystack.pop())
    
    print(finalBinString)

    return finalBinString


def main():
    remainderStack=divisionByTwo(10)
    print("The converted binary number is %s"%returnBinary(remainderStack) )


if __name__=="__main__":
    main()

'''
 Conclusion
            -> I learnt how to call a class from another file. 
            -> OOP really is magic

Happy Learning
'''