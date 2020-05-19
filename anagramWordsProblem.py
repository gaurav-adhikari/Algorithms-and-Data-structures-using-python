# Here I will be implementing the Anagarm problem

# Approach 1
def anagramCheck1(str1,str2):
    
    str1Lst =list(str1)
    str2Lst =list(str2)

    str1Lst.sort()
    str2Lst.sort()


    if (str1Lst==str2Lst):
        return 'Anagram'

    else:
        return 'Not Anagram'

# Approach 2
# The character counting approach
def anagramCheck2(str1,str2):

    strLst1=[0]*26
    strLst2=[0]*26

    # Unicode Calculation process to fill in the index of our above two lists
    for i in range(len(str1)):
        index=ord(str1[i])-ord('a')
        strLst1[index]=strLst1[index]+1

    for i in range(len(str2)):
        index=ord(str2[i])-ord('a')
        strLst2[index]=strLst2[index]+1

    print(strLst1)
    print(strLst2)

    if(strLst1==strLst2):
        return 'Anagram'

    else:
        return 'Not Anagram'


print(anagramCheck1('gaurav','rgauav'))
print(anagramCheck2('gaurav','rgauav'))


'''
 Conclusion
            -> As approach 1 uses inbuilt python functions, In my machine it was approx 1.5 times faster than approach 2
'''
