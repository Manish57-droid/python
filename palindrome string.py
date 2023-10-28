'''WAP to define a fn palin() that accept a string and check whether
it is palindrome'''
def palindrome(str):
    P=str
    Q=str[::-1]
    if P==Q:
        print('Palindrome string')
    else:
        print('Not a palindrome string')
str=input("Enter a string")
palindrome(str)
