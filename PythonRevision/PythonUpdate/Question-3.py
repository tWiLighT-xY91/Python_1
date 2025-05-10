# To print the factorial of a number using recursion

def factorial(n) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = input("Enter the number whose factorial you wish to print ")
print(f"The factorial of the entered number is: {factorial(int(num))}")
