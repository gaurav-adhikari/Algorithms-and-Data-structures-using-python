# An implementation of DeQueues for checking either a given word is palindrome or not

# Importing the custom built DeQueue from another module
from DeQueueImplementation import DeQueue

# CheckPalindrome function implementation 
def checkPalindrome(myWord):

    myQueue = DeQueue()

    for char in myWord:
        myQueue.addRear(char)

    isPalindrome = True

    # Loop through the front and back and check if they are palindrome or not
    while myQueue.size() > 1 and isPalindrome:
        
        if myQueue.removeFront() != myQueue.removeRear():
            isPalindrome = False
            return 'Not Palindrome'

    return 'Palindrome'


def main():

    assert checkPalindrome('radar')=='Palindrome'
    assert checkPalindrome('gaure')!='Palindrome'
    
    pass


if __name__ == '__main__':
    main()


'''
 Conclusion
            -> Implemented palindrome using DeQueues
            -> learned about test cases and it helps you furthur beautify your code
            -> OOP is beautiful

'''