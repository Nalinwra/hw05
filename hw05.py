def calculate(a, operator,  b):
    if b == 0 and operator == "/":
        return None

    if operator not in ["+", "-", "*", "/"]:
        return None
    
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b

def main():
    while True:
        first = input("first number(or q): ")

        if first == "q":
            break
        operator = input("operator(+ - * /): ")
        second = input("second number: ")

        result = calculate(float(first), operator, float(second))
        if result is None:
            print("Cannot calculate that")

        else:
            print(f"result:", result)
main()            