def main():
    number = list(map(int, input("Enter a number who's digit's you'd like the sum of: ")))
    get_sum(number)

def get_sum(n):
    total = sum(n)
    print(total)

main()
