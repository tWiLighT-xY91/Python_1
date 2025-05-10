#To check whether a given number is prime or not

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 1
    return 0


num = input("Enter the number you want to check whether it is prime or not ")
if is_prime(int(num)):
    print("The number you entered is not a prime number.")
else:
    print("The number you entered is a prime number.")
