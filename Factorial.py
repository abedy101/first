def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Enter a number to calculate its factorial: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")

if __name__ == "__main__":
    main()
