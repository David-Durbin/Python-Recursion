
"""
def main():
    message(5)


def message(times):
    if times > 0:
        print('This is a recursive function.')
        message(times - 1)


main()
"""
"""
# Factorial numbers ( n! )
def main():
    # get num from user
    number = int(input('Enter a non-negative integer:  '))

    fact = factorial(number)

    print('The factorial of', number, 'is', format(fact, ',d'))


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


main()
"""
"""
# Fibonacci Numbers  ( a + b = c, b + c = d, c + d = e, d + e = f etc)
def main():
    print("The first 15 non-zero numbers in the Fibonacci series are: ")

    for number in range(1, 16):
        print(fib(number))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


main()
"""


# greatest common divisor
def main():
    num1 = int(input('Enter an integer:  '))
    num2 = int(input('Enter another integer:  '))

    print("The greatest common divisor of those two numbers is: ", gcd(num1, num2))


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)


main()
