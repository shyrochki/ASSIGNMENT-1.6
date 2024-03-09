def add(num1, num2) -> float:
    return num1 + num2


# expected two black lines - between two function, add two blank lines


def subtract(num1, num2) -> float:
    return num1 - num2


def multiply(num1, num2) -> float:
    return num1 * num2

def divide(num1, num2) -> float:
    return num1 / num2


def main():
    print('In order to add, enter "add", in order to subtract, enter "subtract", \
          in order to multiply, enter "multiply", in order to divide, enter "divide"')
    input_operation = input('Enter the operation: ')

    if input_operation not in ['add', 'subtract', 'multiply', 'divide']:
        print('Invalid operation, follow the instructions')
        return

    num1 = float(input('Enter your first number: '))
    num2 = float(input('Enter your second number: '))

    if input_operation == 'add':
        results = add(num1, num2)
        print(f'The result of : {results}')

    if input_operation == 'subtract':
        results = subtract(num1, num2)
        print(f'The result: {results}')

    if input_operation == 'multiply':
        results = multiply(num1, num2)
        print(f'The result: {results}')

    if input_operation == 'divide':
        results = divide(num1, num2)
        print(f'The result of division: {results}')


if __name__ == "__main__":
    main()
