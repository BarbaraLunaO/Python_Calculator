def calculator():
    while True:
        # Get the user's input
        operation = input("Enter an operation (+, -, *, /): ")
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please enter a valid operation.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the requested operation
        if operation == '+':
            print(num1 + num2)
        elif operation == '-':
            print(num1 - num2)
        elif operation == '*':
            print(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            else:
                print(num1 / num2)
        else:
            print("Invalid operation. Please enter a valid operation.")

        # Ask the user if they want to perform another operation
        again = input("Do you want to perform another operation? (y/n) ")
        if again.lower() != 'y':
            break

if __name__ == '__main__':
    calculator()
