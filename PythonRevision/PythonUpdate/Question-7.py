# To reverse a string

def reverse_string(s):
    return s == s[::-1]


s1 = input("Enter the string you want to check if it is palindrome or not: ")
if reverse_string(s1):
    print("Yes, the string is palindrome")
else:
    print("The string is not palindrome")
