def main():
    number = int(input("Enter a whole  number: "))
    get_factorial(number)

def get_factorial(n):
    if n == 0 or n == 1:
        print("The facorial is 1")
    else:
        factorial = 1
        for i in range(factorial, n+1):
            factorial *= i
        print("The factorial is" , factorial)

main()
