def main():
    numbers = list(map(int, input("Enter numbers you'd like stored in the list: ").split()))
    get_sum(numbers)

def get_sum(l):
    total = sum(l)
    print(total)

main()