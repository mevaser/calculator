import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    num1 = float(input("Enter first number: "))

    should_accumulate = True
    while should_accumulate:
        operation = input("Choose an operator ('+', '-', '*', or '/'): ")
        if operation not in operations:
            print("Invalid operator. Please choose a valid one.")
            continue  # Ask for the operator again if it's invalid

        num2 = float(input("Enter second number: "))

        result = operations[operation](num1, num2)

        while isinstance(result, str):  # If the result is an error (e.g., division by zero)
            print(f"{num1} {operation} {num2} = {result}")
            num2 = float(input("Enter a new second number (non-zero for division): "))
            result = operations[operation](num1, num2)  # Recalculate with the new second number

        print(f"{num1} {operation} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculation with {result}, or 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = result  # Continue calculating with the result
        else:
            should_accumulate = False
            print("\n" * 20)  # Clear the screen
            calculator()  # Restart the calculator


calculator()
