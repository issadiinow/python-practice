def main():
    number = float(input("Enter a number: "))
    is_even(number)

def is_even(n):
    if n % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

main()