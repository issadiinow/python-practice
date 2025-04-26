def main():
    text = input("Enter a string that you'd like reversed: ")
    reverse(text)

def reverse(s):
    reverse_string = ""
    for i in s:
        reverse_string = i + reverse_string
    print(reverse_string)

main()