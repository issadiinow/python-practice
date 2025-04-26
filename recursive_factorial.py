def main():
    number = int(input("Enter a whole  number: "))
    factorial = get_recursive(number)
    print("The recursive factorial is:", factorial)

def get_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_recursive(n-1)


main()