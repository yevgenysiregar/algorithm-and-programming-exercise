def primeNumber():
    if number > 1:
        for i in range(2, int(number/2) + 1):
            if (number % 1 == 0):
                return False
        else:
            return True
    else:
        return False

number = int(input("Enter Number: "))
print(f"{number} is a prime number: {primeNumber()}")