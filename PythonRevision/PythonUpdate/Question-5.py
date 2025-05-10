# To reverse a file without using the method reverse()

def reverse_list(listy):
    rev_list = listy[::-1]
    return rev_list


list1 = []
a = 0
print("Enter elements to your list to reverse it: /n (Enter q to stop) ")
while a != 'q':
    a = input("Element: ")
    list1.append(a)
list1.remove('q')
print(f"The reversed version of this list is: {reverse_list(list1)}")
